import pytest
from python.data_loading import load_csv

def test_load_csv_valid_file():
    """Test loading a valid CSV file."""
    import pandas as pd
    data = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [30, 25]})
    data.to_csv("tests/sample_data.csv", index=False)

    loaded_data = load_csv("tests/sample_data.csv")
    assert isinstance(loaded_data, pd.DataFrame)
    assert not loaded_data.empty
    assert "Name" in loaded_data.columns