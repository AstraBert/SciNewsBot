from gnews import GNews
import random
from typing import List, Any, Dict
import pandas as pd

csv = pd.read_csv("/bot/data/mbfc_processed.csv")
sources = csv["source"].to_list()
topics = ["ENVIRONMENT", "SCIENCE", "ENERGY", "TECHNOLOGY"]
google_news = GNews(period="24h")

class NewsArticle:
    def __init__(self, title: str, publisher: Dict[str, str], url: str, topic: str):
        self.title = title
        self.publisher = publisher["title"]
        self.publisher_url = publisher["href"]
        self.topic = topic
        self.url = url

def filter_news(news: List[Dict[str, Any]], topic: str):
    filt_news = [n for n in news if n["publisher"]["href"].replace("https://","") in sources]
    if len(filt_news) > 0:
        random.shuffle(filt_news)
        art = filt_news[0]
        article = NewsArticle(art["title"], art["publisher"], url=art["url"], topic = topic)
        return article
    return None

def get_news(topic: str):
    news = google_news.get_news_by_topic(topic)
    return news, topic