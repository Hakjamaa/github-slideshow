# Automatisation de la Veille Stratégique - Maroc & International

Ce projet automatise la veille stratégique pour le suivi de l'économie, de l'industrie et de la géopolitique (Maroc et International).

## Fonctionnalités

- **Collecte multi-sources** : Flux RSS nationaux (L'Économiste, Médias24, etc.) et internationaux (Reuters, Le Monde, Les Échos, etc.).
- **Analyse thématique** :
    - Secteurs : Industrie, Économie Maroc, Économie Mondiale, Moyen-Orient, Tarifs US, Tech.
    - Évaluation : Identification des **Opportunités** et **Menaces** pour le Maroc.
    - Scoring : Un indice de 0 à 10 basé sur la pertinence stratégique.
- **Export Excel** : Génération d'un tableau récapitulatif avec les colonnes demandées.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python run_veille.py
```

Le fichier Excel sera généré dans le répertoire courant : `veille_strategique_YYYYMMDD.xlsx`.

## Colonnes du rapport

- **Date** : Date de publication de l'article.
- **Organe de presse** : Nom du média source.
- **Titre** : Titre de l'article.
- **Secteur** : Catégories identifiées.
- **Opportunité/Menace** : Analyse rapide du potentiel impact pour le Maroc.
- **Scoring** : Note de pertinence (0-10).
- **Lien** : URL de l'article original.
