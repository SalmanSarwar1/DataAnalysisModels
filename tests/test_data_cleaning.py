from python.data_cleaning import handle_missing_values

def test_handle_missing_values():
    """Test handling missing values."""
    import pandas as pd
    data = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})
    cleaned_data = handle_missing_values(data, strategy="mean")
    assert not cleaned_data.isnull().values.any()