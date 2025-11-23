from textblob import TextBlob
import pandas as pd

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
        if pd.isna(text):
            return 0.0
        return TextBlob(str(text)).sentiment.polarity

    def apply_sentiment_analysis(self) -> pd.DataFrame:
        """
        Applies sentiment scoring to the dataframe.
        """
        print("Calculating sentiment scores...")
        self.df['sentiment_score'] = self.df[self.text_column].apply(self.get_sentiment_score)
        return self.df