
# API Reference

## Data Loader (`src.data_loader`)
**`class DataLoader(data_path)`**
* **Purpose:** Handles the ingestion of raw CSV files and normalization of dates.
* **Methods:**
    * `load_data()`: Returns a cleaned Pandas DataFrame with UTC datetime objects.

## Sentiment Analyzer (`src.sentiment`)
**`class SentimentAnalyzer(df)`**
* **Purpose:** Wraps TextBlob/NLTK logic to apply sentiment scoring to headlines.
* **Methods:**
    * `apply_sentiment_analysis()`: Adds a `sentiment_score` column to the DataFrame.

## Financial Analyzer (`src.analysis`)
**`class FinancialAnalyzer(stock_df, news_df)`**
* **Purpose:** Merges datasets and performs statistical correlation.
* **Methods:**
    * `calculate_daily_returns()`: Computes percentage change on Close price.
    * `merge_and_correlate()`: Aligns data by date and calculates Pearson correlation coefficient.