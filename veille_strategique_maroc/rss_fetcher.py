import feedparser
import logging
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_html(html_content):
    """
    Removes HTML tags and returns plain text.
    """
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator=' ', strip=True)

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

            for entry in feed.entries:
                summary = entry.get('summary', '')
                all_entries.append({
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'summary': clean_html(summary),
                    'source': url
                })
            logging.info(f"Fetched {len(feed.entries)} entries from {url}")
        except Exception as e:
            logging.error(f"Error fetching {url}: {e}")

    return all_entries

if __name__ == "__main__":
    # Example Moroccan news feeds (Economy/Industry focused where possible)
    feeds = [
        "https://www.medias24.com/feed/",
        "https://lematin.ma/rss.xml",
        "https://www.leconomiste.com/rss.xml",
        "https://fr.hespress.com/feed"
    ]

    entries = fetch_rss_feeds(feeds)
    print(f"Total entries fetched: {len(entries)}")
    for entry in entries[:5]:
        print(f"- {entry['title']} ({entry['source']})")
