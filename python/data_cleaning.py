def handle_missing_values(data, strategy="mean", columns=None):
    """Handle missing values in the dataset."""
    if columns is None:
        columns = data.columns
    for column in columns:
        if strategy == "mean":
            data[column].fillna(data[column].mean(), inplace=True)
        elif strategy == "median":
            data[column].fillna(data[column].median(), inplace=True)
        elif strategy == "drop":
            data.dropna(subset=[column], inplace=True)
    return data