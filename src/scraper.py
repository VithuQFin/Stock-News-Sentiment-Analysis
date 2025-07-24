# app/scraper.py

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from http.client import IncompleteRead
from datetime import datetime

def scrape_ticker(ticker: str):
    url = f'https://finviz.com/quote.ashx?t={ticker}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        req = Request(url=url, headers=headers)
        response = urlopen(req)
        html = BeautifulSoup(response, 'html.parser')
        news_table = html.find(id='news-table')
        
        if not news_table:
            return []

        parsed_news = []
        rows = news_table.findAll('tr')
        
        for row in rows:
            title = row.a.text.strip()
            date_data = row.td.text.strip().split(' ')
            
            if len(date_data) == 1:
                date = datetime.today().strftime('%b-%d-%y')
                time = date_data[0]
            else:
                date = date_data[0]
                time = date_data[1]
                if date == 'Today':
                    date = datetime.today().strftime('%b-%d-%y')

            parsed_news.append({
                'ticker': ticker,
                'date': date,
                'time': time,
                'title': title
            })

        return parsed_news

    except IncompleteRead as e:
        print(f"[Error] {ticker}: {e}")
        return []

    except Exception as e:
        print(f"[Unexpected error] {ticker}: {e}")
        return []
