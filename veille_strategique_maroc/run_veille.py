import os
import datetime
import logging
from rss_fetcher import fetch_rss_feeds
from analyzer import analyze_entries

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sources RSS for Morocco Strategic Intelligence
RSS_SOURCES = [
    "https://www.medias24.com/feed/",
    "https://lematin.ma/rss.xml",
    "https://www.leconomiste.com/rss.xml",
    "https://fr.hespress.com/feed",
    "https://www.challenge.ma/feed/",
    "https://lavieeco.com/feed/"
]

def generate_report(categorized_entries, date_str):
    """
    Generates a simple Markdown report based on categorized entries.
    """
    report_content = f"# Rapport de Veille Stratégique - Maroc\n"
    report_content += f"Date: {date_str}\n\n"
    report_content += "Ce rapport automatise la veille sur l'industrie et l'économie au Maroc.\n\n"

    total_found = 0
    for category, entries in categorized_entries.items():
        if entries:
            report_content += f"## {category}\n"
            for entry in entries:
                report_content += f"- **[{entry['title']}]({entry['link']})**\n"
                # report_content += f"  - Source: {entry['source']}\n"
                total_found += 1
            report_content += "\n"

    if total_found == 0:
        report_content += "Aucune actualité pertinente n'a été trouvée pour les critères définis aujourd'hui.\n"

    return report_content

def main():
    logging.info("Starting strategic intelligence pipeline...")

    # 1. Fetch entries
    entries = fetch_rss_feeds(RSS_SOURCES)

    # 2. Analyze and categorize
    categorized, _ = analyze_entries(entries)

    # 3. Generate report
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    report = generate_report(categorized, today)

    # 4. Save report
    report_filename = f"rapport_veille_{datetime.datetime.now().strftime('%Y%m%d')}.md"
    report_path = os.path.join(os.getcwd(), report_filename)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    logging.info(f"Pipeline complete. Report generated: {report_path}")
    print(f"Report successfully generated: {report_path}")

if __name__ == "__main__":
    main()
