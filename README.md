# 📰 Stock News Sentiment Analysis with FinBERT

This project combines **web scraping**, **NLP-based sentiment analysis**, and **financial data**. It scrapes recent headlines from Finviz, analyzes their sentiment using a fine-tuned BERT model (FinBERT).

---

## 🚀 Objectives

- Scrape the latest headlines for a given ticker (e.g., `AMZN`) from **Finviz**
- Use **FinBERT** to classify the sentiment of each news title (positive / neutral / negative)

---

## 🧱 Project Structure

```plaintext
.
NLP/
├── data/
│ └── processed/ # Final datasets (CSV outputs)
│
├── src/
│ ├── scraper.py # Scrapes news headlines from Finviz
│ ├── sentiment.py # Sentiment scoring with FinBERT
│ ├── manager.py # End-to-end processing pipeline
│
├── main.py # Main entry point
├── requirements.txt # Python dependencies
└── .gitignore # Files excluded from Git

---

## 🔁 Processing Pipeline

1. **News Scraping** – from Finviz for the selected ticker
2. **Sentiment Analysis** – using FinBERT for title-level scoring
3. **Export Final Dataset** – as CSV with all scores

---

## 📊 Sample Output

| date       | title                            | score |
|------------|----------------------------------|-------|
| 2025-07-22 | My 3 Favorite Stocks to Buy Now  | 0.61  |
| 2025-07-23 | Alphabet updates AI forecast...  | 0.00  |
| 2025-07-24 | Amazon to acquire AI startup...  | 1.00  |

---

## ⚙️ Installation & Usage

```bash
# Clone the repo
git clone https://github.com/VithuQFin/Stock-Sentiment-Analysis.git
cd Stock-Sentiment-Analysis

# Create & activate environment (conda or venv)
conda create -n sentiment python=3.10
conda activate sentiment

# Install dependencies
pip install -r requirements.txt

# Run main pipeline
python main.py

⚠️ Limitations

    Finviz provides a limited number of headlines per ticker

    Small news sample size → not statistically significant for event studies

    This is a proof-of-concept for combining NLP + financial data
