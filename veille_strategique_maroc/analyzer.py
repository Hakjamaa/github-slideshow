import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Keywords relevant to industry, economy, and global strategic issues
KEYWORDS = {
    "Industrie": ["industrie", "usine", "manufacturier", "production", "automobile", "aéronautique", "agroalimentaire", "OCP", "phosphates", "énergie"],
    "Économie Maroc": ["économie", "PIB", "croissance", "inflation", "budget", "finance", "investissement", "commerce", "exportation", "importation", "Banque Al-Maghrib"],
    "Économie Mondiale": ["économie mondiale", "marchés mondiaux", "récession", "taux d'intérêt", "FED", "BCE", "FMI", "Banque Mondiale"],
    "Moyen-Orient": ["Moyen-Orient", "guerre", "conflit", "pétrole", "gaz", "crise", "géopolitique", "Israël", "Palestine", "Liban", "Iran"],
    "Tarifs US": ["tarifs US", "droits de douane", "Trump", "USA", "Etats-Unis", "commerce international", "protectionnisme"],
    "Politique Économique": ["ministre", "gouvernement", "réforme", "plan", "stratégie", "accord", "partenariat", "investissement étranger", "IDE"],
    "Digital & Tech": ["numérique", "digital", "startup", "technologie", "innovation", "IA", "e-commerce"]
}

# Scoring and Opportunity/Threat logic
STRATEGIC_KEYWORDS = {
    "Opportunité": ["accord", "partenariat", "investissement", "croissance", "développement", "nouveau marché", "exportation", "IDE"],
    "Menace": ["crise", "guerre", "conflit", "inflation", "tarifs", "protectionnisme", "récession", "dépréciation", "instabilité"]
}

def analyze_entries(entries):
    """
    Analyzes RSS entries and categorizes them based on industry and economic keywords.
    """
    analyzed_data = []

    for entry in entries:
        content = (entry['title'] + " " + entry['summary']).lower()

        # 1. Determine Sector(s)
        matched_sectors = []
        for category, terms in KEYWORDS.items():
            if any(term.lower() in content for term in terms):
                matched_sectors.append(category)

        # 2. Opportunity/Threat for Morocco
        opportunity = "Neutre"
        opp_score = sum(1 for term in STRATEGIC_KEYWORDS["Opportunité"] if term.lower() in content)
        threat_score = sum(1 for term in STRATEGIC_KEYWORDS["Menace"] if term.lower() in content)

        if opp_score > threat_score:
            opportunity = "Opportunité"
        elif threat_score > opp_score:
            opportunity = "Menace"

        # 3. Scoring (0-10)
        # Based on how many relevant terms are found
        base_score = len(matched_sectors) * 2 + opp_score + threat_score
        final_score = min(base_score, 10)

        if matched_sectors:
            analyzed_data.append({
                'date': entry.get('published', 'N/A'),
                'source_name': entry.get('source_name', 'Inconnue'),
                'title': entry['title'],
                'link': entry['link'],
                'sectors': ", ".join(matched_sectors),
                'opportunity_threat': opportunity,
                'scoring': final_score,
                'summary': entry['summary']
            })

    return analyzed_data

if __name__ == "__main__":
    # Test sample
    sample_entries = [
        {"title": "Croissance du PIB au Maroc en 2024", "summary": "L'économie marocaine montre des signes de résilience.", "source_name": "Medias24", "link": "http://example.com/1"},
        {"title": "Guerre au Moyen-Orient et impact pétrole", "summary": "Les prix de l'énergie s'envolent.", "source_name": "Reuters", "link": "http://example.com/2"},
        {"title": "Nouveaux tarifs US sur l'aluminium", "summary": "Trump impose des droits de douane.", "source_name": "Bloomberg", "link": "http://example.com/3"}
    ]

    results = analyze_entries(sample_entries)
    for res in results:
        print(f"{res['title']} | Sector: {res['sectors']} | {res['opportunity_threat']} | Score: {res['scoring']}")
