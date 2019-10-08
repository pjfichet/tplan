#! /usr/bin/env python

from .bp import Plan
from .data import *
from .tables import *
import re
import locale
import sys
import os


class Parser():

	def __init__(self, debug = False):
		self.debug = debug
		self.bp = None
		self.cur = None
		self.line = ""
		self.line_number = 0
		self.table_format = ""
		self.table_width = 0

	def error(self, text):
		name = os.path.basename(sys.argv[0])
		print(f"{name} ligne {self.line_number}: {self.line}", file=sys.stderr, end='')
		print(f"    {text}", file=sys.stderr)

	def parse_line(self):
		regex = re.compile(r'^\.\s*bp:(?P<command>\w+)')	
		match = regex.search(self.line)
		if match:
			command = match.group('command')
			return command
		return None	

	def parse(self, infile):
		self.line = infile.readline()
		while self.line:
			self.line_number += 1
			command = self.parse_line()
			if command in classes:
				self.parse_class(command)
			elif command in fields:
				self.parse_field()
			elif command == 'set':
				self.parse_set()
			elif command == 'get':
				self.parse_get()
			elif command == 'tbl':
				self.parse_table()
			elif command is not None:
				self.error(f"Unknown command {command}.")
				if not self.debug:
					print(self.line, end='')
			else:
				if not self.debug:
					print(self.line, end='')
			self.line = infile.readline()

	def parse_class(self, command):
		if command == 'plan':
			self.bp = Plan()
			self.cur = self.bp
		else:
			function = getattr(self.bp, "new_" + command)
			self.cur = function()


	def set_type(self, field, value):
		if field in int_fields:
			value = int(value)	
		elif field in float_fields:
			value = float(value)
		elif field in dict_fields:
			value = [float(i) for i in value.split()]
			if len(value) != 12:
				self.error("Not 12 elements.")
				return []
		if field in percent_fields:
			total = round(sum(value))
			if total != 1:
				self.error(f"Total de {total}.")
				return []
		return value

	def parse_field(self):
		regex = re.compile(r'^\.\s*bp:(?P<field>\w+)\s+(?P<value>.*)\n')
		match = regex.search(self.line)
		if not match:
			self.error("Donnée manquante.")
			return
		field = match.group('field')
		value = match.group('value')
		value = self.set_type(field, value)
		setattr(self.cur, field, value)


	def parse_set(self):
		regex = re.compile(r'^\.\s*bp:set:(?P<classe>\w+):(?P<index>\d+):(?P<field>\w+)\s+(?P<value>.*)\n')
		match = regex.search(self.line)
		if not match:
			self.error("Invalid command set.")
			return
		classe = match.group('classe')
		if classe not in classes:
			self.error(f"Unknown class {classe}.")
			return
		index = int(match.group('index'))
		field = match.group('field')
		if field not in fields:
			self.error(f"Unknown field {field}.")
		value = match.group('value')
		value = self.set_type(field, value)
		try:
			classe = getattr(self.bp, classe)
			setattr(classe[index], field, value)
		except IndexError:
			self.error(f"Index '{index}' out of range.")
			return
		except AttributeError:
			self.error(f"Invalid field {field}.")
			return
		self.bp.reset()

	def parse_get(self):
		regex = re.compile(r'^\.\s*bp:get:(?P<classe>\w+):(?P<index>\d+):(?P<field>\w+)')
		match = regex.search(self.line)
		if not match:
			self.error("Invalid command get.")
			return
		classe = match.group('classe')
		if classe not in classes + other_classes:
			self.error(f"Unknown class {classe}.")
			return
		index = int(match.group('index'))
		field = match.group('field')
		if field not in fields + other_fields:
			self.error(f"Unknown field {field}.")
		self.bp.set()
		try:
			classe = getattr(self.bp, classe)
			value = getattr(classe[index], field)
		except IndexError:
			self.error(f"Index '{index}' out of range.")
			return
		except AttributeError:
			self.error(f"Invalid field {field}.")
			return
		if field in float_fields + other_float_fields:
			value=int(round(value))
			value = format(value, 'n')
		before = ""
		after = ""
		regex = re.compile(r'^\.\s*bp:get:(?P<classe>\w+):(?P<index>\d+):(?P<field>\w+)\s+(?P<after>\S*)')
		match = regex.search(self.line)
		if match:
			after = match.group('after') 
		regex = re.compile(r'^\.\s*bp:get:(?P<classe>\w+):(?P<index>\d+):(?P<field>\w+)\s+(?P<after>\S*)\s+(?P<before>\S*)')
		match = regex.search(self.line)
		if match:
			before = match.group('before') 
		print(f"{before}{value}{after}")

	def parse_table(self):
		regex = re.compile(r'^\.\s*bp:tbl:(?P<table>\w+)\s+(?P<fields>.*)')
		match = regex.search(self.line)
		if not match:
			self.error("Invalid command tbl.")
			return
		table = match.group('table')
		fields = match.group('fields')
		if table not in tables:
			self.error(f"Unknown table {table}.")
		if table == 'format':
			self.table_format = fields	
			width = re.sub('[c]', '', fields)
			self.table_width = sum(int(i) for i in width.split())
			return
		annees = [int(i) for i in fields.split()]
		mois = [int(i)*12-1 for i in fields.split()]
		columns = [int(i)-1 for i in fields.split()]
		self.bp.set()
		if table == 'resultat':
			self.header("Compte de résultat")
			self.annee(annees)
			self.table(self.bp.resultat, resultat_rows, columns)
		elif table == 'exploitation':
			self.header("Compte d'exploitation")
			self.table(self.bp.tresorerie, exploitation_rows, columns)
		elif table == 'tresorerie':
			self.header("Trésorerie")
			self.mois(self.bp.tresorerie, columns)
			self.table(self.bp.tresorerie, tresorerie_rows, columns)
		elif table == 'bfr':
			self.header("Besoin en fonds de roulement")
			self.mois(self.bp.tresorerie, columns)
			self.table(self.bp.tresorerie, bfr_rows, columns)
		elif table == 'frais':
			self.header("Frais")
			self.table_frais(annees)

	def header(self, header):
		if self.debug:
			return
		print(".tblbeg", str(self.table_width) + 'c')
		print(".tblbox 0 1 1")
		print(".tblmac tbl:cb")
		print(".tblrow", '"' + header + '"')
		print(".tblrec", self.table_format)

	def mois(self, data, mois):
		if self.debug:
			return
		print(".tblmac tbl:c", end='')
		for m in mois:
			print(" tbl:c", end='')
		print('')
		print(f'.tblrow "\&"', end='')
		for m in mois:
			nom = mois_list[data[m].mois_reel -1]
			print(f' "{nom}"', end='')
		print('')
				
	def annee(self, annees):
		if self.debug:
			return
		print(".tblmac tbl:c", end='')
		for an in annees:
			print(" tbl:c", end='')
		print('')
		print(f'.tblrow "\&"', end='')
		for an in annees:
			print(f' "année {an}"', end='')
		print('')

	def table(self, data, rows, columns):
		if self.debug:
			return
		print(".tblmac tbl:l", end='')
		for col in columns:
			print(" tbl:r", end='')
		print('')
		for row in rows:
			key = row[0]
			label = row[1]
			if re.match("tbl:.*", key):
				print(f".tblmac {key}", end="")
				for col in columns:
					print(f" {label}", end="")
				print("")
			else:
				print(f'.tblrow "{label}"', end='')
				for col in columns:
					value = round(getattr(data[col], key))
					value = format(value, 'n')
					print(f' "{value}"', end='')
				print('')
		print(".tblend")

	def table_frais(self, annees):
		if self.debug:
			return
		self.annee(annees)
		done = []
		for frais in self.bp.frais:
			nom = frais.nom
			if nom in done:
				continue
			done.append(nom)
			print(f'.tblrow "{nom}"', end="")
			for annee in annees:
				get = self.bp.get_frais(nom, annee)
				if get is None:
					montant = 0
				else:
					montant = get.montant
				print(f" {montant}", end="")
			print('')
		print(".tblend")



