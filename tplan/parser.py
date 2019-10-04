#! /usr/bin/env python

from .bp import Plan
import re
import locale
import sys


regex_prefix = re.compile(r'^\.\s*bp:')	
regex_dict = {
	# 	'#': re.compile(r'^\.\s*bp:#\s*\n'),
	# Classes
	'plan': re.compile(r'^\.\s*bp:plan\s*\n'),
	'produit': re.compile(r'^\.\s*bp:produit\s*\n'),
	'personnel': re.compile(r'^\.\s*bp:personnel\s*\n'),
	'frais': re.compile(r'^\.\s*bp:frais\s*\n'),
	'impot': re.compile(r'^\.\s*bp:impot\s*\n'),
	'investissement': re.compile(r'^\.\s*bp:investissement\s*\n'),
	'capital': re.compile(r'^\.\s*bp:capital\s*\n'),
	'subvention_exploitation': re.compile(r'^\.\s*bp:subvention_exploitation\s*\n'),
	'subvention_investissement': re.compile(r'^\.\s*bp:subvention_investissement\s*\n'),
	'emprunt': re.compile(r'^\.\s*bp:emprunt\s*\n'),

	# Data
	'nom': re.compile(r'^\.\s*bp:nom\s+(?P<nom>.*)\n'),
	'duree': re.compile(r'^\.\s*bp:duree\s+(?P<duree>.*)\n'),
	'annee': re.compile(r'^\.\s*bp:annee\s+(?P<annee>.*)\n'),
	'mois': re.compile(r'^\.\s*bp:mois\s+(?P<mois>.*)\n'),
	'chiffre_affaire': re.compile(r'^\.\s*bp:chiffre_affaire\s+(?P<chiffre_affaire>.*)\n'),
	'tva': re.compile(r'^\.\s*bp:tva\s+(?P<tva>.*)\n'),
	'prix_achat': re.compile(r'^\.\s*bp:prix_achat\s+(?P<prix_achat>.*)\n'),
	'delai_fournisseur': re.compile(r'^\.\s*bp:delai_fournisseur\s+(?P<delai_fournisseur>.*)\n'),
	'delai_client': re.compile(r'^\.\s*bp:delai_client\s+(?P<delai_client>.*)\n'),
	'achats': re.compile(r'^\.\s*bp:achats\s+(?P<achats>.*)\n'),
	'ventes': re.compile(r'^\.\s*bp:ventes\s+(?P<ventes>.*)\n'),
	'etp': re.compile(r'^\.\s*bp:etp\s+(?P<etp>.*)\n'),
	'embauche': re.compile(r'^\.\s*bp:embauche\s+(?P<embauche>.*)\n'),
	'salaire_brut': re.compile(r'^\.\s*bp:salaire_brut\s+(?P<salaire_brut>.*)\n'),
	'charges_salariales': re.compile(r'^\.\s*bp:charges_salariales\s+(?P<charges_salariales>.*)\n'),
	'charges_patronales': re.compile(r'^\.\s*bp:charges_patronales\s+(?P<charges_patronales>.*)\n'),
	'montant': re.compile(r'^\.\s*bp:montant\s+(?P<montant>.*)\n'),
	'calendrier': re.compile(r'^\.\s*bp:calendrier\s+(?P<calendrier>.*)\n'),
	'taux': re.compile(r'^\.\s*bp:taux\s+(?P<taux>.*)\n'),
	'nb_echeances_annuelles': re.compile(r'^\.\s*bp:nb_echeances_annuelles\s+(?P<nb_echeances_annuelles>.*)\n'),
	# Commands
	'tbl': re.compile(r'^\.\s*bp:tbl\s+(?P<tbl>.*)\n'),
	'resultat': re.compile(r'^\.\s*bp:resultat\s+(?P<resultat>.*)\n'),
	'tresorerie': re.compile(r'^\.\s*bp:tresorerie\s+(?P<tresorerie>.*)\n'),
	'exploitation': re.compile(r'^\.\s*bp:exploitation\s+(?P<exploitation>.*)\n'),
	'bfr': re.compile(r'^\.\s*bp:bfr\s+(?P<bfr>.*)\n'),
	'pfrais': re.compile(r'^\.\s*bp:pfrais\s+(?P<pfrais>.*)\n')
}

resultat_rows = [
	['chiffre_affaire', "Chiffre d'affaire"],
	['achat_marchandise', "Achat marchandises"],
	['variation_marchandise', "Variation stock marchandise"],
	['tbl:lb', "tbl:rb"],
	['marge_commerciale', "Marge commerciale"],
	['tbl:l', "tbl:r"],
	['frais', "Autres achats"],
	['subvention_exploitation', "Subventions d'exploitation"],
	['tbl:lb', "tbl:rb"],
	['valeur_ajoutee', "Valeur ajoutée"],
	["tbl:l", "tbl:r"],
	['impot', "Impôts et taxes"],
	['salaire_net', "Salaires nets"],
	['charges_sociales', "Charges sociales"],
	['excedent', "Excédent brut d'exploitation"],
	['amortissement', "Dotation aux amortissements"],
	['resultat_exploitation', "Résultat d'exploitation"],
	['emprunt_interets', "Intérêts des emprunts"],
	["tbl:lb", "tbl:rb"],
	['resultat_courant', "Résultat courant"],
	["tbl:l", "tbl:r"],
	['produits_exceptionnels', "Produits exceptionnels"],
	['impot_societes', "Impôt sur les sociétés"],
	["tbl:lb", "tbl:rb"],
	['resultat_net', "Résultat net"],
	["tbl:l", "tbl:r"],
	['autofinancement', "Autofinancement"]
]

bilan_rows = [
	["actif_immobilise", "Actif immobilisé net"],
	["immobilisations_brutes", "Immobilisations brutes"],
	["amortissements", "Amortissements"],
	["actif_circulant", "Actif circulant"],
	["stock", "Stock"],
	["creances_clients", "Créances clients"],
	["autres_creances", "Autres créances"],
	["disponibilites", "Disponibilités"],
	["total_actif", "Total actif"],
	["capitaux_propres", "Capitaux propres"],
	["capital_social", "Capital social"],
	["reserves", "Réserves"],
	["resultat_net", "Résultat net"],
	["subvention_investissement", "Subventions d'investissements"],
	["dettes", "Dettes"],
	["emprunts", "Emprunts à moyen et long terme"],
	["fournisseurs", "Fournisseurs"],
	["dettes_fiscales", "Dettes fiscales et sociales"],
	["total_passif", "Total passif"]
]

exploitation_rows = [
	["cumul_stock", "Stock marchandises"],
	["creances_clients", "Créances clients"],
	["credit_tva", "Créances TVA"],
	["creances_fiscales", "Créances fiscales"],
	['tbl:lb', "tbl:rb"],
	["total_creances", "Total créances"],
	['tbl:l', "tbl:r"],
	["dettes_fournisseurs", "Comptes fournisseurs"],
	["debit_tva", "TVA à payer"],
	["dettes_fiscales", "Dettes fiscales"],
	["dettes_sociales", "Dettes sociales"],
	['tbl:lb', "tbl:rb"],
	["total_dettes", "Total dettes"],
	["bfr", "Besoin en fonds de roulement"],
	['tbl:l', "tbl:r"],
	["variation_bfr_annuel", "Variation de BFR"],
	["chiffre_affaire_annuel", "Chiffre d'affaire"],
	["bfr_jours_ca", "BFR en jours de CA"]
]

bfr_rows = [
	["cumul_stock", "Stock marchandises"],
	["variation_stock", "Variation stock"],
	["creances_clients", "Créances clients"],
	["credit_tva", "Créances TVA"],
	["creances_fiscales", "Créances fiscales"],
	['tbl:lb', "tbl:rb"],
	["total_creances", "Total créances"],
	['tbl:l', "tbl:r"],
	["variation_creances", "Variation créances"],
	["dettes_fournisseurs", "Comptes fournisseurs"],
	["debit_tva", "TVA à payer"],
	["dettes_fiscales", "Dettes fiscales"],
	["dettes_sociales", "Dettes sociales"],
	['tbl:lb', "tbl:rb"],
	["total_dettes", "Total dettes"],
	['tbl:l', "tbl:r"],
	["variation_dettes", "Variation dettes"],
	['tbl:lb', "tbl:rb"],
	["bfr", "Besoin en fonds de roulement"],
	['tbl:l', "tbl:r"],
	["variation_bfr", "Variation de BFR"]
]


tresorerie_rows = [
	["ventes", "Clients TTC"],
	["apport", "Capital et subventions"],
	["emprunt", "Emprunts"],
	['tbl:lb', "tbl:rb"],
	["entrees", "Total encaissements"],
	['tbl:l', "tbl:r"],
	["achats", "Achats TTC"],
	["frais", "Frais généraux TTC"],
	["tva", "TVA à payer"],
	["salaires_net", "Salaires"],
	["charges_sociales", "Cotisations sociales"],
	["investissement", "Investissements TTC"],
	["remboursement", "Remboursements d'emprunts"],
	["impot", "Impôts"],
	['tbl:lb', "tbl:rb"],
	["sorties", "Total décaissements"],
	['tbl:l', "tbl:r"],
	["solde_mensuel", "Solde mensuel"],
	['tbl:lb', "tbl:rb"],
	["solde_cumul", "Solde cumulé"],
	['tbl:l', "tbl:r"]
]

mois_list = [ 'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
	'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']




class Parser():

	def __init__(self, debug = False):
		self.debug = debug
		self.bp = None
		self.cur = None
		self.line = 0
		self.format = ""
		self.width = 0

	def error(self, text):
		print(f"{sys.argv[0]}, ligne {self.line}:", text, file=sys.stderr)

	def parse_line(self, line):
		match = regex_prefix.search(line)
		if match:
			for key, regex in regex_dict.items():
				match = regex.search(line)
				if match:
					return key, match
		return None, None	

	def parse(self, fileobject):
		line = fileobject.readline()
		while line:
			self.line += 1
			key, match = self.parse_line(line)
			if not self.debug:
				print(line, end='')
			line = fileobject.readline()
			if key is None:
				continue	
			# classes
			elif key == 'plan':
				self.bp = Plan()
				self.cur = self.bp
			elif key == 'produit':
				self.cur = self.bp.new_produit()
			elif key == 'personnel':
				self.cur = self.bp.new_personnel()
			elif key == 'frais':
				self.cur = self.bp.new_frais()
			elif key == 'impot':
				self.cur = self.bp.new_impot()
			elif key == 'investissement':
				self.cur = self.bp.new_investissement()
			elif key == 'capital':
				self.cur = self.bp.new_capital()
			elif key == 'subvention_exploitation':
				self.cur = self.bp.new_subvention_exploitation()
			elif key == 'subvention_investissement':
				self.cur = self.bp.new_subvention_investissement()
			elif key == 'emprunt':
				self.cur = self.bp.new_emprunt()
			# datas
			else:
				data = match.group(key)
				if key == 'nom':
					self.cur.nom = data
				elif key == 'duree':
					self.cur.duree = int(data)
				elif key == 'annee':
					self.cur.annee = int(data)
				elif key == 'mois':
					self.cur.mois = int(data)
				elif key == 'chiffre_affaire':
					self.cur.chiffre_affaire = float(data)
				elif key == 'tva':
					self.cur.tva = float(data)
				elif key == 'prix_achat':
					self.cur.prix_achat = float(data)
				elif key == 'delai_fournisseur':
					self.cur.delai_fournisseur = int(data)
				elif key == 'delai_client':
					self.cur.delai_client = int(data)
				elif key == 'achats':
					self.cur.achats = [float(i) for i in data.split()]
					elems = len(self.cur.achats)
					if elems != 12:
						self.error(f"Achats invalides ({elems} éléments)")
				elif key == 'ventes':
					self.cur.ventes = [float(i) for i in data.split()]
					elems = len(self.cur.ventes)
					if elems != 12:
						self.error(f"Ventes invalides ({elems} éléments)")
					total = round(sum(self.cur.ventes))
					if total != 1:
						self.error(f"Ventes invalides (total de {total}).")
				elif key == 'etp':
					self.cur.etp = float(data)
				elif key == 'embauche':
					self.cur.embauche = int(data)
				elif key == 'salaire_brut':	
					self.cur.salaire_brut = float(data)
				elif key == 'charges_salariales':
					self.cur.charges_salariales = float(data)
				elif key == 'charges_patronales':
					self.cur.charges_patronales = float(data)
				elif key == 'duree':
					self.cur.duree = int(data)
				elif key == 'montant':
					self.cur.montant = int(data)
				elif key == 'calendrier':
					self.cur.calendrier = [float(i) for i in data.split()]
					elems = len(self.cur.calendrier)
					if elems != 12:
						self.error(f"calendrier invalide ({elems} éléments)")
				elif key == 'taux':
					self.cur.taux = float(data)
				elif key == 'nb_echeances_annuelles':
					self.cur.nb_echeances_annuelles = int(data)
				# commands
				elif key == 'tbl':
					self.format = data
					width = re.sub('[c]', '', data)
					self.width = sum(int(i) for i in width.split())
				elif key == 'resultat':
					self.bp.set_resultat()
					self.header("Compte de résultat")
					annees = [int(i) for i in data.split()]
					self.annee(annees)
					columns = [int(i)-1 for i in data.split()]
					self.table(self.bp.resultat, resultat_rows, columns)
				elif key == 'exploitation':
					self.bp.set_tresorerie()
					self.header("Compte d'exploitation")
					annees = [int(i) for i in data.split()]
					self.annee(annees)
					columns = [int(i)*12-1 for i in data.split()]
					self.table(self.bp.tresorerie, exploitation_rows, columns)
				elif key == 'tresorerie':
					self.bp.set_tresorerie()
					self.header("Trésorerie")
					columns = [int(i)-1 for i in data.split()]
					self.mois(self.bp.tresorerie, columns)
					self.table(self.bp.tresorerie, tresorerie_rows, columns)
				elif key == 'bfr':
					self.bp.set_tresorerie()
					self.header("Besoin en fonds de roulement")
					columns = [int(i)-1 for i in data.split()]
					self.mois(self.bp.tresorerie, columns)
					self.table(self.bp.tresorerie, bfr_rows, columns)
				elif key == 'pfrais':
					self.bp.set_resultat()
					self.header("Frais")
					print(f'.tblrow "Frais" "montant"')
					for frais in self.bp.frais:
						nom = frais.nom
						montant = int(round(frais.montant))
						print(f'.tblrow "{nom}" "{montant}"')
					print(f'.tblend')


	def header(self, header):
		if self.debug:
			return
		print(".tblbeg", str(self.width) + 'c')
		print(".tblbox 0 1 1")
		print(".tblmac tbl:cb")
		print(".tblrow", '"' + header + '"')
		print(".tblrec", self.format)




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
