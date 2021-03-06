tables = ['format', 'resultat', 'exploitation', 'tresorerie', 'bfr',
	'tva', 'frais', 'investissements', 'ventes']


resultat_rows = [
	['chiffre_affaire', "+ Chiffre d'affaires"],
	['achat_marchandise', "\- Achat marchandises"],
	['variation_marchandise', "+ Variation stock marchandise"],
	['tbl:lb', "tbl:rb"],
	['marge_commerciale', "Marge commerciale"],
	['tbl:l', "tbl:r"],
	['frais', "\- Autres achats"],
	['tbl:lb', "tbl:rb"],
	['valeur_ajoutee', "Valeur ajoutée"],
	["tbl:l", "tbl:r"],
	['subvention_exploitation', "+ Subventions d'exploitation"],
	['impot', "\- Impôts et taxes"],
	['salaire_brut', "\- Salaires bruts"],
	['charges_patronales', "\- Charges sociales"],
	['tbl:lb', "tbl:rb"],
	['excedent', "Excédent brut d'exploitation"],
	["tbl:l", "tbl:r"],
	['amortissement', "\- Dotation aux amortissements"],
	['tbl:lb', "tbl:rb"],
	['resultat_exploitation', "Résultat d'exploitation"],
	["tbl:l", "tbl:r"],
	['emprunt_interets', "\- Intérêts des emprunts"],
	["tbl:lb", "tbl:rb"],
	['resultat_courant', "Résultat courant"],
	["tbl:l", "tbl:r"],
	['produits_exceptionnels', "+ Produits exceptionnels"],
	['tbl:lb', "tbl:rb"],
	['resultat_brut', "Résultat avant impôt"],
	["tbl:l", "tbl:r"],
	['impot_societes', "\- Impôt sur les bénéfices"],
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

tva_rows = [
	["tva_ventes", "TVA sur ventes"],
	["tva_achats", "TVA sur achats"],
	["tva_frais", "TVA sur frais"],
	["tva_investissement", "TVA sur investissements"],
	["credit_tva", "Crédit de TVA"],
	["debit_tva", "Débit de TVA"],
	["tva", "TVA due"]
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
	["salaires_net", "Salaires net"],
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


