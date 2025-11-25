# src/sentiment.py
import pandas as pd
from textblob import TextBlob

class SentimentAnalyzer:
    """
    Handles sentiment analysis on text data.
    """
    def __init__(self, df: pd.DataFrame, text_column: str = 'headline'):
        self.df = df
        self.text_column = text_column

    def get_sentiment_score(self, text: str) -> float:
        """
        Returns a polarity score between -1 (negative) and 1 (positive).
        """
        try:
            return TextBlob(str(text)).sentiment.polarity
        except Exception:
            return 0.0

    def apply_sentiment_analysis(self) -> pd.DataFrame:
        """
        Applies sentiment scoring to the dataframe.
        """
        self.df['sentiment_score'] = self.df[self.text_column].apply(self.get_sentiment_score)
        return self.df