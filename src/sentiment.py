# app/sentiment.py

from transformers import BertTokenizer, BertForSequenceClassification
import torch.nn.functional as F
import torch
import numpy as np

# Initialisation globale
MODEL_NAME = 'yiyanghkust/finbert-tone'
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
finbert = BertForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=3)
labels_map = {0: 'neutral', 1: 'positive', 2: 'negative'}

def analyze_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = finbert(**inputs).logits
    probs = F.softmax(outputs[0], dim=0)
    label_index = torch.argmax(probs).item()
    label = labels_map[label_index]
    score = probs[label_index].item()
    
    # Convention : négatif → score négatif
    signed_score = score if label == 'positive' else (-score if label == 'negative' else 0.0)

    return {
        'label': label,
        'score': signed_score,
        'probs': probs.tolist()
    }
