import os
import datetime
import logging
import pandas as pd
from rss_fetcher import fetch_rss_feeds
from analyzer import analyze_entries

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sources RSS for Strategic Intelligence (Moroccan & International)
RSS_SOURCES = [
    # Morocco
    "https://www.medias24.com/feed/",
    "https://lematin.ma/rss.xml",
    "https://www.leconomiste.com/rss.xml",
    "https://fr.hespress.com/feed",
    "https://www.challenge.ma/feed/",
    "https://lavieeco.com/feed/",
    # International
    "https://www.reutersagency.com/feed/?taxonomy=reuters_topic&term=business",
    "https://www.lemonde.fr/international/rss_full.xml",
    "https://www.lesechos.fr/rss/rss_monde.xml",
    "https://www.economist.com/international/rss.xml",
    "https://feeds.aawsat.com/index.php/feed/world",
]

def main():
    logging.info("Starting strategic intelligence pipeline...")

    # 1. Fetch entries
    entries = fetch_rss_feeds(RSS_SOURCES)

    # 2. Analyze and categorize
    results = analyze_entries(entries)

    if not results:
        logging.info("No relevant results found.")
        print("No relevant results found today.")
        return

    # 3. Create DataFrame
    df = pd.DataFrame(results)

    # Select and reorder columns as requested
    final_df = df[['date', 'source_name', 'title', 'sectors', 'opportunity_threat', 'scoring', 'link']]
    final_df.columns = ['Date', 'Organe de presse', 'Titre', 'Secteur', 'Opportunité/Menace', 'Scoring', 'Lien']

    # 4. Save to Excel
    today_str = datetime.datetime.now().strftime('%Y%m%d')
    excel_filename = f"veille_strategique_{today_str}.xlsx"
    excel_path = os.path.join(os.getcwd(), excel_filename)

    try:
        final_df.to_excel(excel_path, index=False, engine='openpyxl')
        logging.info(f"Report exported to Excel: {excel_path}")
        print(f"Excel report successfully generated: {excel_path}")
    except Exception as e:
        logging.error(f"Error exporting to Excel: {e}")
        # Fallback to CSV
        csv_path = excel_path.replace('.xlsx', '.csv')
        final_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        logging.info(f"Report exported to CSV as fallback: {csv_path}")

if __name__ == "__main__":
    main()
