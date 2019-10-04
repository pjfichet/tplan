#! /usr/bin/env python

from dataclasses import dataclass, field
from typing import List
from .data import *


@dataclass
class Plan():
	nom: str = "Plan d'affaire"
	duree: int = 1
	annee: int = 1
	mois: int = 1
	produit: List[Produit] = field(default_factory=list)
	personnel: List[Personnel] =  field(default_factory=list)
	frais: List[Divers] = field(default_factory=list)
	impot: List[Divers] = field(default_factory=list)
	investissement: List[Divers] = field(default_factory=list)
	capital: List[Divers] = field(default_factory=list)
	subvention_exploitation: List[Divers] = field(default_factory=list)
	subvention_investissement: List[Divers] = field(default_factory=list)
	emprunt: List[Emprunt] = field(default_factory=list)
	remboursement: List[Remboursement] = field(default_factory=list)
	resultat: List[Resultat] = field(default_factory=list)
	tresorerie: List[Tresorerie] = field(default_factory=list)
	has_emprunt: bool = False
	has_resultat: bool = False
	has_tresorerie: bool = False

	def new_produit(self):
		self.produit.append(Produit())
		return self.produit[-1]

	def new_personnel(self):
		self.personnel.append(Personnel())
		return self.personnel[-1]

	def new_frais(self):
		self.frais.append(Divers())
		return self.frais[-1]

	def new_impot(self):
		self.impot.append(Divers())
		return self.impot[-1]

	def new_investissement(self):
		self.investissement.append(Divers())
		return self.investissement[-1]

	def new_capital(self):
		self.capital.append(Divers())
		return self.capital[-1]

	def new_subvention_exploitation(self):
		self.subvention_exploitation.append(Divers())
		return self.subvention_exploitation[-1]

	def new_subvention_investissement(self):
		self.subvention_investissement.append(Divers())
		return self.subvention_investissement[-1]

	def new_emprunt(self):
		self.emprunt.append(Emprunt())
		return self.emprunt[-1]

	def new_remboursement(self):
		self.remboursement.append(Remboursement())
		return self.remboursement[-1]

	def new_resultat(self):
		self.resultat.append(Resultat())
		return self.resultat[-1]

	def new_tresorerie(self):
		self.tresorerie.append(Tresorerie())
		return self.tresorerie[-1]

	def get_tresorerie(self, cumul_mois):
		for cal in self.tresorerie:
			if cal.cumul_mois == cumul_mois:
				return cal

	def get_remboursement(self, cumul_mois):
		for remboursement in self.remboursement:
			if remboursement.cumul_mois == cumul_mois:
				return remboursement

	def set_emprunt(self):
		# This has to be done only once
		if self.has_emprunt:
			return
		for emprunt in self.emprunt:
			emprunt.mois_debut = 12*(emprunt.annee - 1) + emprunt.mois
			emprunt.mois_fin = emprunt.mois_debut + 12*emprunt.duree
			emprunt.nb_echeances_annuelles = 12
			emprunt.nb_echeances = emprunt.duree * emprunt.nb_echeances_annuelles
			emprunt.taux_periodique = emprunt.taux / emprunt.nb_echeances_annuelles
			emprunt.montant_echeance = emprunt.montant * emprunt.taux_periodique \
				/ (1 - (1+emprunt.taux_periodique) ** (-emprunt.nb_echeances) )

			cumul_mois = 0
			for i in range(self.duree):
				annee = i + 1
				for j in range(12):
					mois = j + 1
					cumul_mois += 1
					remboursement = self.new_remboursement()
					remboursement.nom = emprunt.nom
					remboursement.annee = annee
					remboursement.mois = mois
					remboursement.cumul_mois = cumul_mois
					remboursement.nb_echeances_payees = cumul_mois - emprunt.mois_debut + 1
					remboursement.cumul_echeances = remboursement.nb_echeances_payees * emprunt.montant_echeance
					remboursement.cumul_capital = emprunt.montant \
						* ((1+emprunt.taux_periodique) ** (remboursement.nb_echeances_payees) -1) \
						/ ((1+emprunt.taux_periodique) ** (emprunt.nb_echeances) -1)
					remboursement.cumul_interet = remboursement.cumul_echeances - remboursement.cumul_capital
					if remboursement.cumul_mois == emprunt.mois_debut:
						remboursement.echeance = remboursement.cumul_echeances
						remboursement.capital = remboursement.cumul_capital
						remboursement.interet = remboursement.cumul_interet
					else:
						for pre in self.remboursement:
							if pre.cumul_mois == remboursement.cumul_mois -1 and pre.nom == remboursement.nom:
								remboursement.echeance = remboursement.cumul_echeances - pre.cumul_echeances
								remboursement.capital = remboursement.cumul_capital - pre.cumul_capital
								remboursement.interet = remboursement.cumul_interet - pre.cumul_interet
				

			#for i in range(self.duree):
			#	annee = i + 1
			#	remboursement = self.new_remboursement()
			#	remboursement.nom = emprunt.nom
			#	remboursement.annee = annee
			#	if emprunt.annee <= remboursement.annee:
			#		duree = remboursement.annee - emprunt.annee + 1
			#		remboursement.cumul_echeances = duree * emprunt.echeances_annuelles * emprunt.echeance
			#		remboursement.cumul_capital = emprunt.montant \
			#			* ((1+emprunt.taux_periodique) ** (duree * emprunt.echeances_annuelles) -1) \
			#			/ ((1+emprunt.taux_periodique) ** (emprunt.echeances) -1)
			#		remboursement.cumul_interet = remboursement.cumul_echeances - remboursement.cumul_capital
			#		if remboursement.annee == 1:
			#			remboursement.echeances = remboursement.cumul_echeances
			#			remboursement.capital = remboursement.cumul_capital
			#			remboursement.interet = remboursement.cumul_interet
			#		else:
			#			for pre in self.remboursement:
			#				if pre.annee == remboursement.annee -1 and pre.nom == remboursement.nom:
			#					remboursement.echeances = remboursement.cumul_echeances - pre.cumul_echeances
			#					remboursement.capital = remboursement.cumul_capital - pre.cumul_capital
			#					remboursement.interet = remboursement.cumul_interet - pre.cumul_interet
		self.has_emprunt = True



	def set_resultat(self):
		if self.has_resultat:
			return
		self.set_emprunt()
		for i in range(self.duree):
			resultat = self.new_resultat()
			resultat.annee = i + 1
			resultat.annee_reelle = self.annee + i
			for produit in self.produit:
				if produit.annee == resultat.annee:
					resultat.chiffre_affaire += produit.chiffre_affaire
					resultat.achat_marchandise += produit.chiffre_affaire* produit.prix_achat
					resultat.achat_marchandise += sum(produit.achats)
					resultat.variation_marchandise -= sum(produit.achats)

			for personnel in self.personnel:
				if personnel.annee == resultat.annee:
					nb_mois = 13 - personnel.embauche
					resultat.salaire_brut += nb_mois * personnel.salaire_brut
					resultat.charges_salariales = resultat.salaire_brut * personnel.charges_salariales
					resultat.charges_patronales = resultat.salaire_brut * personnel.charges_patronales
					resultat.salaire_net = resultat.salaire_brut - resultat.charges_salariales
					resultat.salaire = resultat.salaire_brut + resultat.charges_patronales

			for frais in self.frais:
				if frais.annee == resultat.annee:
					frais.montant = sum(frais.calendrier)
					resultat.frais += frais.montant

			for impot in self.impot:
				if impot.annee == resultat.annee:
					impot.montant = sum(impot.calendrier)
					resultat.impot += impot.montant

			for investissement in self.investissement:
				if investissement.annee == resultat.annee:
					investissement.montant = sum(investissement.calendrier)
					resultat.investissement += investissement.montant
				if resultat.annee <= investissement.annee + investissement.duree:
					resultat.amortissement += sum(investissement.calendrier) / investissement.duree

			for capital in self.capital:
				if capital.annee == resultat.annee:
					capital.montant = sum(capital.calendrier)
					resultat.capital += capital.montant

			for subvention in self.subvention_exploitation:
				if subvention.annee == resultat.annee:
					subvention.montant = sum(subvention.calendrier)
					resultat.subvention_exploitation += subvention.montant

			for subvention in self.subvention_investissement:
				if subvention.annee == resultat.annee:
					subvention.montant = sum(subvention.calendrier)
					resultat.subvention_investissement += subvention.montant
				if resultat.annee == subvention.annee:
					resultat.amortissement_subventions += subvention.montant / 8
				elif resultat.annee <= subvention.annee + 4:
					resultat.amortissement_subventions += subvention.montant / 4

			for remboursement in self.remboursement:
				if remboursement.cumul_mois == resultat.annee * 12:
					resultat.emprunt_echeances += remboursement.cumul_echeances
					resultat.emprunt_capital += remboursement.cumul_capital
					resultat.emprunt_interets += remboursement.cumul_interet
					pre = self.get_remboursement((resultat.annee - 1) * 12)
					if pre is not None:
						resultat.emprunt_echeances -= pre.cumul_echeances
						resultat.emprunt_capital -= pre.cumul_capital
						resultat.emprunt_interets -= pre.cumul_interet
				
			resultat.marge_commerciale = resultat.chiffre_affaire - resultat.achat_marchandise - resultat.variation_marchandise
			resultat.charges_sociales = resultat.charges_salariales + resultat.charges_patronales
			resultat.valeur_ajoutee = resultat.marge_commerciale + resultat.subvention_exploitation - resultat.frais
			resultat.excedent = resultat.valeur_ajoutee - resultat.impot - resultat.salaire_brut - resultat.charges_patronales
			resultat.resultat_exploitation = resultat.excedent - resultat.amortissement
			resultat.resultat_courant = resultat.resultat_exploitation - resultat.emprunt_interets
			resultat.produits_exceptionnels = resultat.amortissement_subventions
			resultat.impot_societes = (resultat.resultat_courant + resultat.produits_exceptionnels)*0.15
			resultat.resultat_net = resultat.resultat_courant + resultat.produits_exceptionnels - resultat.impot_societes
			resultat.autofinancement = resultat.resultat_net + resultat.amortissement - resultat.amortissement_subventions
		self.has_resultat = True

	def set_tresorerie(self):
		if self.has_tresorerie:
			return
		self.set_emprunt()
		cumul_mois = 0
		for an in range(self.duree):
			for mois in range(12):
				cal = self.new_tresorerie()			
				cal.annee = an + 1
				cal.mois = mois + 1
				cal.annee_reelle = an + self.annee
				cal.mois_reel = mois + self.mois
				if cal.mois_reel > 12:
					cal.mois_reel -= 12
					cal.annee_reelle += 1
				cumul_mois += 1
				cal.cumul_mois = cumul_mois

		for cal in self.tresorerie:
			for produit in self.produit:
				if produit.annee == cal.annee:
					cal.chiffre_affaire += produit.chiffre_affaire * produit.ventes[cal.mois -1]
					# la tva est comptabilisée à la date de facturation
					cal.tva_ventes += produit.chiffre_affaire * produit.tva * produit.ventes[cal.mois -1]
					cal.tva_achats += produit.chiffre_affaire * produit.tva * produit.prix_achat * produit.ventes[cal.mois -1] \
						+ produit.achats[cal.mois -1] * produit.tva
					cal.variation_stock += produit.achats[cal.mois -1] # * (1+produit.tva)
					# On paie les achats à l'expiration du délai fournisseur
					mois_paiement = int(cal.cumul_mois + produit.delai_fournisseur/30)
					get = self.get_tresorerie(mois_paiement)
					if get is not None:
						achats = produit.chiffre_affaire * (1+produit.tva) * produit.prix_achat * produit.ventes[cal.mois -1] \
							+ produit.achats[cal.mois -1] * (1+produit.tva)
						get.achats += achats
					# On acccumule une dette fournisseur
					if cal.cumul_mois != mois_paiement:
						for mois in range(cal.cumul_mois, mois_paiement):
							get = self.get_tresorerie(mois)
							if get is not None:
								get.dettes_fournisseurs += achats
					# On accumule les créances clients
					mois_paiement = int(cal.cumul_mois + produit.delai_client/30)
					get = self.get_tresorerie(mois_paiement)
					if get is not None:
						get.ventes += produit.chiffre_affaire * (1+produit.tva) * produit.ventes[cal.mois -1]
					if cal.cumul_mois != mois_paiement:
						for mois in range(cal.cumul_mois, mois_paiement):
							get = self.get_tresorerie(mois)
							if get is not None:
								get.creances_clients +=  produit.chiffre_affaire * (1+produit.tva) * produit.ventes[cal.mois -1]
	
			for apport in self.capital + self.subvention_investissement + self.subvention_exploitation:
				if apport.annee == cal.annee:
					cal.apport += apport.calendrier[cal.mois -1]

			for emprunt in self.emprunt:
				if emprunt.mois_debut == cal.cumul_mois:
					cal.emprunt += emprunt.montant
				if emprunt.mois_debut <= cal.cumul_mois and cal.cumul_mois <= emprunt.mois_fin:
					cal.remboursement += emprunt.montant_echeance


			for frais in self.frais:
				if frais.annee == cal.annee:
					cal.frais += frais.calendrier[cal.mois -1] * (1+frais.tva)
					cal.tva_frais += frais.calendrier[cal.mois -1] * frais.tva

			for impot in self.impot:
				if impot.annee == cal.annee:
					cal.impot += impot.calendrier[cal.mois -1]

			for personnel in self.personnel:
				if personnel.annee == cal.annee and personnel.embauche <= cal.mois:
					cal.salaires_net += personnel.salaire_brut*(1-personnel.charges_salariales) * personnel.etp
					cal.dettes_sociales += personnel.salaire_brut*(personnel.charges_salariales + personnel.charges_patronales) * personnel.etp

			for investissement in self.investissement:
				if investissement.annee == cal.annee:
					cal.investissement += investissement.calendrier[cal.mois -1] * (1+investissement.tva)
					#tva_investissement == tva_immobilisation
					cal.tva_investissement += investissement.calendrier[cal.mois -1] * investissement.tva

			tva = cal.tva_achats + cal.tva_frais + cal.tva_investissement - cal.tva_ventes
			if tva >= 0:
				cal.credit_tva = tva
			else:
				cal.debit_tva = -tva
			cal.cumul_dettes_sociales = cal.dettes_sociales - cal.charges_sociales
			# Set values based on previous month
			cal.charges_sociales = 0
			cal.solde_cumul = cal.solde_mensuel
			cal.cumul_stock = cal.variation_stock
			cal.total_creances = cal.creances_clients + cal.credit_tva
			cal.variation_creances = cal.total_creances
			cal.total_dettes = cal.dettes_fournisseurs + cal.dettes_sociales + cal.debit_tva
			cal.variation_dettes = cal.total_dettes

			pre = self.get_tresorerie(cal.cumul_mois -1)
			if pre is not None:
				cal.chiffre_affaire_annuel = cal.chiffre_affaire + pre.chiffre_affaire_annuel
				cal.charges_sociales = pre.dettes_sociales
				cal.solde_cumul = pre.solde_cumul + cal.solde_mensuel
				# tva
				cal.tva = pre.debit_tva
				if pre.credit_tva + tva >= 0:
					cal.credit_tva = pre.credit_tva + tva
					cal.debit_tva = 0
				else:
					cal.credit_tva = 0
					cal.debit_tva = - (pre.credit_tva + tva)
				# variation bfr
				cal.cumul_stock = pre.cumul_stock + cal.variation_stock
				cal.total_creances = cal.creances_clients + cal.credit_tva
				cal.variation_creances = cal.total_creances - pre.total_creances
				cal.total_dettes = cal.dettes_fournisseurs + cal.dettes_sociales + cal.debit_tva
				cal.variation_dettes = cal.total_dettes - pre.total_dettes
			cal.bfr = cal.cumul_stock + cal.total_creances - cal.total_dettes 
			cal.variation_bfr = cal.variation_stock + cal.variation_creances - cal.variation_dettes

			cal.entrees = cal.ventes + cal.apport + cal.emprunt
			cal.sorties = cal.achats + cal.frais + cal.impot + cal.salaires_net \
				+ cal.charges_sociales + cal.investissement \
				+ cal.remboursement + cal.tva
			cal.solde_mensuel = cal.entrees - cal.sorties
			cal.solde_cumul = cal.solde_mensuel
			if pre is not None:
				cal.solde_cumul = pre.solde_cumul + cal.solde_mensuel

			if cal.cumul_mois == 1 or cal.cumul_mois -1 % 12 == 0:
				cal.chiffre_affaire_annuel = cal.chiffre_affaire
			if cal.chiffre_affaire_annuel != 0:
				cal.bfr_jours_ca = cal.bfr / (cal.chiffre_affaire_annuel / 365)
		
			cal.variation_bfr_annuel = cal.bfr	
			pre = self.get_tresorerie(cal.cumul_mois -12)
			if pre is not None:
				cal.variation_bfr_annuel = cal.bfr - pre.bfr

		self.has_tresorerie = True

