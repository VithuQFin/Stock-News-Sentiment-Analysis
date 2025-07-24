from src.manager import (
    fetch_and_analyze,
)
import os

# ✅ Fix OpenMP warning for FinBERT
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == "__main__":
    ticker = "AMZN"

    # 📰 Étape 1 — Scraping + NLP
    df_news = fetch_and_analyze(ticker)

    # 💾 Étape 4 — Export CSV
    output_path = f"data/processed/{ticker}_sentiment.csv"
    df_news.to_csv(output_path, index=False)
    print(f"✅ Données sauvegardées dans : {output_path}\n")
