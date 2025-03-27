def generate_descriptive_statistics(data):
    """Generate descriptive statistics for a given dataset."""
    return data.describe()

def plot_histogram(data, column, bins=10):
    """Plot a histogram for a specified column in the dataset."""
    import matplotlib.pyplot as plt
    plt.hist(data[column], bins=bins, alpha=0.7)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()