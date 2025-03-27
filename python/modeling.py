from sklearn.linear_model import LinearRegression

def train_linear_model(data, x_column, y_column):
    """Train a linear regression model."""
    X = data[[x_column]]
    y = data[y_column]
    model = LinearRegression()
    model.fit(X, y)
    return model