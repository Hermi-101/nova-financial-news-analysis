import pandas as pd
import talib

class FinancialAnalyzer:
    def __init__(self, stock_df: pd.DataFrame, news_df: pd.DataFrame):
        self.stock_df = stock_df
        self.news_df = news_df

    def calculate_daily_returns(self):
        self.stock_df['Daily_Return'] = self.stock_df['Close'].pct_change()
        return self.stock_df

    def aggregate_sentiment_by_date(self):
        """Average sentiment scores by date to match daily stock data."""
        # Ensure date columns match formats (normalize to date only)
        self.news_df['date_only'] = self.news_df['date'].dt.date
        daily_sentiment = self.news_df.groupby('date_only')['sentiment_score'].mean().reset_index()
        return daily_sentiment

    def merge_and_correlate(self):
        """Merges datasets and calculates Pearson correlation."""
        daily_sentiment = self.aggregate_sentiment_by_date()
        
        # Prepare stock data
        self.stock_df['date_only'] = self.stock_df.index.date
        
        merged_df = pd.merge(self.stock_df, daily_sentiment, on='date_only', how='inner')
        
        correlation = merged_df['Daily_Return'].corr(merged_df['sentiment_score'])
        return correlation, merged_df