import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
nltk.download('stopwords')
# Load raw, clean text (remove URLs, lemmatize, etc.)
df = pd.read_csv('data/raw/reddit_comments.csv')
# Preprocessing logic here: df['clean_text'] = ...
train, test = train_test_split(df, test_size=0.2, random_state=42)
train.to_csv('data/processed/train.csv', index=False)
test.to_csv('data/processed/test.csv', index=False)