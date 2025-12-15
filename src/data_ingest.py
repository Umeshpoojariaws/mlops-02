import pandas as pd
# Example: Download or load local CSV
df = pd.read_csv('https://example.com/reddit_comments.csv')  # Or local path
df.to_csv('data/raw/reddit_comments.csv', index=False)