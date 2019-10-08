#! /usr/bin/env python

from dataclasses import dataclass, field
from typing import List

classes = ['plan', 'produit', 'personnel', 'frais', 'impot',
	'investissement', 'capital', 'subvention_exploitation',
	'subvention_investissement', 'emprunt']


other_classes = ['resultat', 'tresorerie']

fields = ['nom', 'duree', 'annee', 'mois', 'chiffre_affaire', 'tva',
	'prix_achat', 'delai_fournisseur', 'delai_client', 'achats',
	'ventes', 'etp', 'embauche', 'salaire_brut', 'charges_salariales',
	'charges_patronales', 'montant', 'calendrier', 'taux',
'nb_echeances_annuelles']


other_fields = ['annee_relle', 'chiffre_affaire', 'achat_marchandise',
'variation_marchandise', 'marge_commerciale', 'frais', 'impot',
'investissement', 'amortissement', 'capital', 'salaire_brut',
'salaire_net', 'charges_salariales', 'charges_patronales',
'charges_sociales', 'subvention_exploitation',
'subvention_investissement', 'amortissement_subventions',
'emprunt_echeances', 'emprunt_capital', 'emprunt_interets',
'valeur_ajoutee', 'excedent', 'resultat_exploitation',
'resultat_courant', 'produits_exceptionnels', 'impot_societes',
'resultat_net', 'autofinancement', 'annee', 'mois', 'cumul_mois',
'mois_reel', 'annee_reelle', 'ventes', 'tva_ventes', 'achats',
'tva_achats', 'chiffre_affaire', 'chiffre_affaire_annuel',
'variation_stock', 'cumul_stock', 'apport', 'emprunt',
'remboursement', 'frais', 'impot', 'tva_frais', 'salaires_net',
'dettes_sociales', 'charges_sociales', 'investissement',
'tva_investissement', 'entrees', 'sorties', 'solde_mensuel',
'solde_cumul', 'credit_tva', 'debit_tva', 'tva', 'creances_clients',
'dettes_fournisseurs', 'creances_fiscales', 'dettes_fiscales',
'cumul_dettes_sociales', 'total_creances', 'variation_creances',
'total_dettes', 'variation_dettes', 'bfr', 'variation_bfr',
'variation_bfr_annuel', 'bfr_jours_ca',]


int_fields = ['duree', 'annee', 'mois', 'delai_fournisseur',
	'delai_client', 'embauche', 'duree', 'montant', 'nb_echeances_annuelles']
float_fields = ['chiffre_affaire', 'tva', 'prix_achat', 'etp',
	'salaire_brut', 'charges_salariales', 'charges_patronales',
	'taux']

other_float_fields = [
	'achat_marchandise', 'variation_marchandise', 'marge_commerciale',
	'frais', 'impot', 'investissement', 'amortissement', 'capital',
	'salaire_brut', 'salaire_net', 'charges_salariales',
	'charges_patronales', 'charges_sociales', 'subvention_exploitation',
	'subvention_investissement', 'amortissement_subventions',
	'emprunt_echeances', 'emprunt_capital', 'emprunt_interets',
	'valeur_ajoutee', 'excedent', 'resultat_exploitation',
	'resultat_courant', 'produits_exceptionnels', 'impot_societes',
	'resultat_net', 'autofinancement', 'tva_ventes',
	'tva_achats', 'chiffre_affaire_annuel', 'variation_stock',
	'cumul_stock', 'apport', 'emprunt', 'remboursement', 'frais', 'impot',
	'tva_frais', 'salaires_net', 'dettes_sociales', 'charges_sociales',
	'investissement', 'tva_investissement', 'entrees', 'sorties',
	'solde_mensuel', 'solde_cumul', 'credit_tva', 'debit_tva', 'tva',
	'creances_clients', 'dettes_fournisseurs', 'creances_fiscales',
	'dettes_fiscales', 'cumul_dettes_sociales', 'total_creances',
	'variation_creances', 'total_dettes', 'variation_dettes', 'bfr',
	'variation_bfr', 'variation_bfr_annuel', 'bfr_jours_ca']

dict_fields = ['achats', 'ventes', 'calendrier']
percent_fields = ['ventes',]


@dataclass
class Produit():
	nom: str = ''
	annee: int = 0
	chiffre_affaire: float = 0
	tva: float = 0
	prix_achat: float = 0
	delai_fournisseur: int = 0
	delai_client: int = 0
	achats: list = field(default_factory=list)
	ventes: list = field(default_factory=list)

@dataclass
class Personnel():
	nom: str = ''
	annee: int = 0
	etp: int = 0
	embauche: int = 0
	salaire_brut: float = 0
	charges_salariales: float = 0
	charges_patronales: float = 0

@dataclass
class Divers():
	nom: str = ''
	annee: int = 0
	tva: float = 0
	duree: float = 0
	montant: float = 0
	calendrier: list = field(default_factory=list)

@dataclass
class Emprunt():
	nom: str = ''
	annee: int = 0
	mois: int = 0
	mois_debut: int = 0
	mois_fin: int = 0
	montant: float = 0
	duree: int = 0
	taux: float = 0
	nb_echeances_annuelles: int = 0
	nb_echeances: int = 0
	taux_periodique: float = 0
	montant_echeance: float = 0

@dataclass
class Remboursement():
	nom: str = ''
	annee: int = 0
	mois: int = 0
	cumul_mois: int = 0
	nb_echeances_payees: int = 0
	cumul_capital: float = 0
	cumul_echeances: float = 0
	cumul_interet: float = 0
	echeance: float = 0
	capital: float = 0
	interet: float = 0
	
@dataclass
class Resultat():
	annee: int = 1
	annee_relle: int = 2000
	chiffre_affaire: float = 0
	achat_marchandise: float = 0
	variation_marchandise: float = 0
	marge_commerciale: float = 0
	frais: float = 0
	impot: float = 0
	investissement: float = 0
	amortissement: float = 0
	capital: float = 0
	salaire_brut: float = 0
	salaire_net: float = 0
	charges_salariales: float = 0
	charges_patronales: float = 0
	charges_sociales: float = 0
	subvention_exploitation: float = 0
	subvention_investissement: float = 0
	amortissement_subventions: float = 0
	emprunt_echeances: float = 0
	emprunt_capital: float = 0
	emprunt_interets: float = 0
	valeur_ajoutee: float = 0
	excedent: float = 0
	resultat_exploitation: float = 0
	resultat_courant: float = 0
	produits_exceptionnels: float = 0
	impot_societes: float = 0
	resultat_net: float = 0
	autofinancement: float = 0

@dataclass
class Tresorerie():
	annee: int = 1
	mois: int = 1
	cumul_mois: int = 1
	mois_reel: int = 1
	annee_reelle: int = 2000
	ventes: float = 0 # ca * (1+tva) * pourcentage
	tva_ventes: float = 0 # ca * tva * pourcentage
	achats: float = 0 # (vente from cumul_mois - round(delai_fournisseur / 30) * (1+tva) * pourcentage * prix_achat
					# + stock from round(delai_fournisseur/30) * (1+tva) * prix_achat
	tva_achats: float = 0 # tva_ventes * prix_achat + tva_stock * prix_achat
	chiffre_affaire: float = 0 # chiffre d'affaire du mois
	chiffre_affaire_annuel: float = 0 # chiffre d'affaire cumulé annuel	
	variation_stock: float = 0 #achats pour le stock
	cumul_stock: float = 0 # état du stock
	apport: float = 0 # capital, subventions
	emprunt: float = 0 # montant emprunt
	remboursement: float = 0 # mensualite
	frais: float = 0 # montant * (1+tva)
	impot: float = 0 # montant
	tva_frais: float = 0 # montant*tva
	salaires_net: float = 0 # salaire_brut*(1-charges_salariales) * effectif
	dettes_sociales: float = 0 # salaire_brut * effectif * (charges_patronales = charges_salariales)
	charges_sociales: float = 0 # dettes sociales mois précédent
	investissement: float = 0 # montant * (1+tva)
	# tva_investissement = tva_immobilisations
	tva_investissement: float = 0 # montant * tva
	entrees: float = 0 # ventes + apport + emprunts + subventions
	sorties: float = 0 # achats + frais + salaries + charges_sociales + investissements + remboursement
	solde_mensuel: float = 0 # entrees - sorties
	solde_cumul: float = 0 # cumul mois précédent + solde_mensuel
	credit_tva: float = 0 # crédit tva s'accumule
	debit_tva: float = 0 # à payer le mois prochain
	tva: float = 0 # à payer du mois précédent
	creances_clients: float = 0 # ca*(1+tva)*pourcentage where mois_vente <= mois courant < mois courant + délai_client/30
				# = pour tous les achats non encore payés
	dettes_fournisseurs: float = 0 # ca*(1+tva)*pourcentage*prix_achat
	creances_fiscales: float = 0 # not implemented
	dettes_fiscales: float = 0 # not implemented
				# pour toutes les ventes non encore payées (délai client non expiré)
	cumul_dettes_sociales: float = 0 # sum(dettes_sociales) - sum(charges_sociales)
	total_creances: float = 0 # compte client + créance tva + créance fiscale
	variation_creances: float = 0 # total_créances - total_créances mois_précéent
	total_dettes: float = 0 # compte fournisseur + tva à payer + dettes fiscales + dettes sociales
	variation_dettes: float = 0 # total_dettes - total_dettes mois précédent
	bfr: float = 0 # total_stock + total_creances - total_dettes
	variation_bfr: float = 0 # variation_stock + variation_créance - variation_dettes
	variation_bfr_annuel: float = 0 # bfr - bfr 12 mois avant
	bfr_jours_ca: float = 0 # cumul_chiffre_affaire_annuel / bfr
	

