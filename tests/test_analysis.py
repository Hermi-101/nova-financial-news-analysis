import pytest
import pandas as pd
from src.data_loader import DataLoader
import os

# Create a temporary CSV file for testing
@pytest.fixture
def mock_csv(tmp_path):
    d = tmp_path / "test_data.csv"
    df = pd.DataFrame({
        'headline': ['Stock rises', 'Market crash'],
        'date': ['2023-01-01', '2023-01-02']
    })
    df.to_csv(d, index=False)
    return str(d)

def test_load_data_exists(mock_csv):
    """Test if data loads correctly from a CSV."""
    loader = DataLoader(mock_csv)
    df = loader.load_data()
    assert not df.empty
    assert 'headline' in df.columns
    assert len(df) == 2

def test_date_conversion(mock_csv):
    """Test if dates are converted to datetime objects."""
    loader = DataLoader(mock_csv)
    df = loader.load_data()
    # Check if the column is a datetime type
    assert pd.api.types.is_datetime64_any_dtype(df['date'])