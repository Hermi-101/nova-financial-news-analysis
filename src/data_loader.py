import pandas as pd
import os

class DataLoader:
    """
    A class to handle data loading and initial preprocessing.
    """
    def __init__(self, data_path: str):
        """
        Initialize the loader with a path to the dataset.
        :param data_path: Path to the CSV file.
        """
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        """
        Loads the dataset and converts dates to datetime objects.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"The file {self.data_path} does not exist.")
            
        df = pd.read_csv(self.data_path)
        
        # Standardize date column
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)
            
        return df