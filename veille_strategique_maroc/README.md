# Automatisation de la Veille Stratégique - Maroc

Ce projet contient des scripts Python pour automatiser la collecte et l'analyse d'informations stratégiques concernant l'industrie et l'économie au Maroc.

## Fonctionnalités

- **Collecte multi-sources** : Récupère les actualités via les flux RSS des principaux médias économiques marocains (L'Économiste, Médias24, Le Matin, Challenge, etc.).
- **Analyse thématique** : Filtre et catégorise automatiquement les articles en fonction de mots-clés stratégiques (Industrie, Économie, Digital, Politique Économique).
- **Génération de rapport** : Produit un rapport quotidien au format Markdown récapitulant les informations pertinentes trouvées.

## Installation

1. Assurez-vous d'avoir Python 3 installé.
2. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Pour lancer la veille et générer le rapport du jour, exécutez le script principal :

```bash
python run_veille.py
```

Le rapport sera généré dans le répertoire courant sous le nom `rapport_veille_YYYYMMDD.md`.

## Structure du projet

- `rss_fetcher.py` : Gère la récupération des flux RSS.
- `analyzer.py` : Contient la logique de filtrage et de catégorisation.
- `run_veille.py` : Script principal orchestrant le pipeline complet.
- `requirements.txt` : Liste des bibliothèques Python nécessaires.
