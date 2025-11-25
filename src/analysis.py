import pandas as pd
import numpy as np

class FinancialAnalyzer:
    def __init__(self, stock_df: pd.DataFrame, news_df: pd.DataFrame):
        self.stock_df = stock_df
        self.news_df = news_df
        
        # --- FIX: Flatten MultiIndex columns from yfinance ---
        # This prevents the "arg must be a list..." TypeError
        if isinstance(self.stock_df.columns, pd.MultiIndex):
            self.stock_df.columns = self.stock_df.columns.get_level_values(0)

    def normalize_dates(self):
        """
        Ensures both dataframes have a standardized 'date_only' column.
        """
        # Convert index to column if necessary
        if self.stock_df.index.name == 'Date':
             self.stock_df = self.stock_df.reset_index()
        
        # Create date_only column for stock data
        if 'Date' in self.stock_df.columns:
             self.stock_df['date_only'] = pd.to_datetime(self.stock_df['Date']).dt.date
        elif 'date' in self.stock_df.columns:
             self.stock_df['date_only'] = pd.to_datetime(self.stock_df['date']).dt.date

        # Create date_only column for news data
        self.news_df['date_only'] = pd.to_datetime(self.news_df['date']).dt.date

    def calculate_daily_returns(self):
        """
        Computes the daily percentage change in stock price.
        """
        # Now this will work because 'Close' is guaranteed to be a single column
        self.stock_df['Close'] = pd.to_numeric(self.stock_df['Close'], errors='coerce')
        self.stock_df['Daily_Return'] = self.stock_df['Close'].pct_change()
        return self.stock_df

    def aggregate_sentiment(self):
        """
        Aggregates news sentiment by day (mean score).
        """
        daily_sentiment = self.news_df.groupby('date_only')['sentiment_score'].mean().reset_index()
        return daily_sentiment

    def correlation_analysis(self):
        """
        Merges datasets and calculates the Pearson correlation coefficient.
        """
        self.normalize_dates()
        self.calculate_daily_returns()
        daily_sentiment = self.aggregate_sentiment()

        # Merge on the normalized date
        merged_df = pd.merge(self.stock_df, daily_sentiment, on='date_only', how='inner')

        # Drop NaNs created by pct_change (first row)
        merged_df.dropna(subset=['Daily_Return', 'sentiment_score'], inplace=True)

        # Calculate Pearson Correlation
        correlation = merged_df['Daily_Return'].corr(merged_df['sentiment_score'])
        
        return correlation, merged_df