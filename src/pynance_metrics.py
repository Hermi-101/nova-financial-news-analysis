import pandas as pd
from pynance import *
import numpy as np

def calculate_portfolio_metrics(returns_df, risk_free_rate=0.0):
    """
    Calculates key portfolio performance metrics using PyNance.

    Args:
        returns_df (pd.DataFrame): DataFrame of daily percentage returns.
                                   Expected to have stock tickers as columns.
        risk_free_rate (float): Annual risk-free rate (default 0.0 for simplicity).

    Returns:
        pd.Series: A Series containing metrics like Sharpe Ratio, Volatility, etc.
    """
    
    # PyNance expects returns as decimal, not percentage (0.01 instead of 1%)
    decimal_returns = returns_df / 100 
    
    # 1. Calculate Portfolio Returns (Assuming Equal Weighting for simplicity)
    # The 'returns_df' needs to be prepared to ensure it only contains numeric return data
    if decimal_returns.shape[1] > 0:
        portfolio_returns = decimal_returns.mean(axis=1)
    else:
        # Handle case where only one stock is analyzed
        if len(decimal_returns.columns) == 1:
            portfolio_returns = decimal_returns.iloc[:, 0]
        else:
            print("Error: No valid stock return columns found for PyNance analysis.")
            return pd.Series({'Sharpe Ratio': np.nan, 'Volatility': np.nan})


    # 2. Use PyNance to compute metrics
    # Note: pynance.statistics.sharpe_ratio uses the annualization factor (252 days) by default.
    try:
        sharpe = statistics.sharpe_ratio(portfolio_returns, risk_free=risk_free_rate)
        
        metrics = {
            'PyNance_Sharpe_Ratio': sharpe,
            # We can also compute Annualized Volatility
            'PyNance_Annualized_Vol': statistics.volatility(portfolio_returns, annualize=True),
        }
        
        return pd.Series(metrics)
    
    except Exception as e:
        print(f"PyNance calculation error: {e}")
        return pd.Series({'Sharpe Ratio': np.nan, 'Volatility': np.nan})


