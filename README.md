# Predicting Stock Price Moves with News Sentiment 📈


**Week 1 Challenge - Nova Financial Solutions**

## 📖 Project Overview
This project aims to enhance **Nova Financial Solutions'** predictive analytics capabilities by analyzing the correlation between financial news sentiment and stock market movements. Using the **Financial News and Stock Price Integration Dataset (FNSPID)**, we apply Natural Language Processing (NLP) to news headlines and Quantitative Analysis to historical stock prices to discover actionable investment signals.

The goal is to determine if the sentiment of financial news (Positive/Negative) has a statistically significant predictive power over daily stock returns.

## 📂 Repository Structure
This repository follows a modular production-grade structure separating analysis notebooks from reusable source code.

```text
├── .github/workflows/  # CI/CD Pipeline (GitHub Actions)
├── docs/               # Technical documentation & reports
│   ├── methodology.md  # Detailed analysis strategy
│   └── api_reference.md# Documentation for src modules
├── notebooks/          # Jupyter Notebooks for EDA & Prototyping
│   ├── 1_eda_financial_news.ipynb
│   └── 2_quantitative_analysis.ipynb
├── reports/            # Interim and Final PDF/Markdown reports
├── src/                # Reusable Python modules
│   ├── __init__.py
│   ├── data_loader.py  # Data ingestion and cleaning
│   ├── analysis.py     # Technical indicators & correlation logic
│   └── sentiment.py    # Sentiment scoring pipeline
├── tests/              # Unit tests
│   ├── __init__.py
│   └── test_data_loader.py
├── .gitignore          # Files to ignore (data, envs)
├── README.md           # Project entry point
└── requirements.txt    # Python dependencies

Installation & Setup
Prerequisites
Python 3.10 or higher

Git

1. Clone the Repository
Bash

git clone [https://github.com/Hermi-101/nova-financial-news-analysis.git]

2. Create Virtual Environment
Bash

# Windows
python -m venv venv
source venv/Scripts/activate

Methodology
We employ a multi-stage analysis pipeline:

Data Engineering: Loading and cleaning the FNSPID dataset and fetching market data via yfinance.

Exploratory Data Analysis (EDA): Analyzing publication frequency, publisher activity, and headline text statistics.

Quantitative Analysis: Calculating Technical Indicators using TA-Lib:

SMA (Simple Moving Average): 20 & 50-day windows for trend detection.

RSI (Relative Strength Index): Momentum oscillator (Overbought/Oversold).

MACD: Trend-following momentum indicator.

Sentiment Analysis (In Progress): Using NLTK/VADER to score headlines (-1 to +1).

Correlation: Measuring the Pearson correlation between daily aggregated sentiment and next-day stock returns.

For a deep dive, see docs/methodology.md.

Interim Findings (Task 1 & 2)
Data Volume: The dataset contains headlines from over 100 unique publishers.

Publisher Dominance: The top 5 publishers account for the majority of news flow.

Seasonality: News publication frequency correlates strongly with market open hours (13:00 - 20:00 UTC).

Stock Trends: Technical analysis of AAPL reveals clear trend signals using SMA crossovers during the analysis period.

🧪 Running Tests
This project uses pytest for unit testing. To verify the environment and code integrity:
pytest

Authors
[Hermela Angaw] - Data Analyst, Nova Financial Solutions

📄 License
This project is licensed under the MIT License.