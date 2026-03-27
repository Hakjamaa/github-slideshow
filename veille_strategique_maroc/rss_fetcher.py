import feedparser
import logging
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_html(html_content):
    """
    Removes HTML tags and returns plain text.
    """
    if not html_content:
        return ""
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text(separator=' ', strip=True)
    except Exception:
        return html_content

def fetch_rss_feeds(feed_urls):
    """
    Fetches articles from a list of RSS feed URLs.
    """
    all_entries = []
    for url in feed_urls:
        logging.info(f"Fetching feed: {url}")
        try:
            feed = feedparser.parse(url)
            if feed.bozo:
                logging.warning(f"Possible issue with feed {url}: {feed.bozo_exception}")

            # Extract source name from URL if not provided by feed
            domain = urlparse(url).netloc
            source_name = feed.get('feed', {}).get('title', domain)

            for entry in feed.entries:
                summary = entry.get('summary', '') or entry.get('description', '')
                all_entries.append({
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'published': entry.get('published', entry.get('updated', 'N/A')),
                    'summary': clean_html(summary),
                    'source': url,
                    'source_name': source_name
                })
            logging.info(f"Fetched {len(feed.entries)} entries from {url}")
        except Exception as e:
            logging.error(f"Error fetching {url}: {e}")

    return all_entries

if __name__ == "__main__":
    # Sample feeds
    feeds = [
        "https://www.medias24.com/feed/",
        "https://lematin.ma/rss.xml",
        "https://www.leconomiste.com/rss.xml",
        "https://fr.hespress.com/feed",
        "https://feeds.reuters.com/reuters/worldNews",
        "https://www.ft.com/?format=rss",
        "https://www.lesechos.fr/rss/rss_france.xml"
    ]

    entries = fetch_rss_feeds(feeds)
    print(f"Total entries fetched: {len(entries)}")
    for entry in entries[:5]:
        print(f"- {entry['title']} ({entry['source_name']})")
