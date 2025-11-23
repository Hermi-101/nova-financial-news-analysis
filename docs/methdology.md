# Methodology and Analysis Strategy

## 1. Sentiment Analysis Approach
We utilize **NLTK/VADER (Valence Aware Dictionary and sEntiment Reasoner)** for this project.
* **Reasoning:** VADER is specifically attuned to sentiment in short texts and social media, making it ideal for financial headlines which are often brief and emotionally charged (e.g., "plummets", "surges").
* **Scoring:** We focus on the **Compound Score**, normalizing sentiment between -1 (Extreme Negative) and +1 (Extreme Positive).

## 2. Quantitative Financial Analysis
To measure stock performance, we calculate the following technical indicators using **TA-Lib**:
* **SMA (Simple Moving Average):** 20-day and 50-day windows to identify trend direction.
* **RSI (Relative Strength Index):** To detect overbought (>70) or oversold (<30) conditions.
* **MACD:** To identify momentum shifts.

## 3. Correlation Strategy
We align news sentiment with stock returns on a **daily basis**.
* **Lagged Analysis:** We also check if sentiment on Day *T* correlates with returns on Day *T+1* to assess predictive power.