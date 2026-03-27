import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Keywords relevant to industry and economy in Morocco
KEYWORDS = {
    "Industrie": ["industrie", "usine", "manufacturier", "production", "automobile", "aéronautique", "agroalimentaire", "OCP", "phosphates", "énergie"],
    "Économie": ["économie", "PIB", "croissance", "inflation", "budget", "finance", "investissement", "commerce", "exportation", "importation", "Banque Al-Maghrib"],
    "Politique Économique": ["ministre", "gouvernement", "réforme", "plan", "stratégie", "accord", "partenariat", "investissement étranger", "IDE"],
    "Digital & Tech": ["numérique", "digital", "startup", "technologie", "innovation", "IA", "e-commerce"]
}

def analyze_entries(entries):
    """
    Analyzes RSS entries and categorizes them based on industry and economic keywords.
    """
    categorized_data = {category: [] for category in KEYWORDS.keys()}
    uncategorized = []

    for entry in entries:
        content = (entry['title'] + " " + entry['summary']).lower()
        matched = False

        for category, terms in KEYWORDS.items():
            if any(term.lower() in content for term in terms):
                categorized_data[category].append(entry)
                matched = True

        if not matched:
            uncategorized.append(entry)

    return categorized_data, uncategorized

if __name__ == "__main__":
    # Test sample
    sample_entries = [
        {"title": "Croissance du PIB au Maroc en 2024", "summary": "L'économie marocaine montre des signes de résilience.", "source": "test.xml"},
        {"title": "Nouvelle usine automobile à Tanger", "summary": "L'industrie automobile continue de croître.", "source": "test.xml"},
        {"title": "Résultats sportifs", "summary": "Le Maroc gagne un match.", "source": "test.xml"}
    ]

    categorized, others = analyze_entries(sample_entries)
    for cat, items in categorized.items():
        print(f"{cat}: {len(items)}")
    print(f"Autres: {len(others)}")
