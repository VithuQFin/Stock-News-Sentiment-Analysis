# app/manager.py

from src.scraper import scrape_ticker
from src.sentiment import analyze_sentiment
import pandas as pd

def fetch_and_analyze(ticker: str):
    news_items = scrape_ticker(ticker)
    results = []

    for item in news_items:
        analysis = analyze_sentiment(item['title'])
        results.append({
            **item,
            'sentiment': analysis['label'],
            'score': analysis['score']
        })

    return pd.DataFrame(results)