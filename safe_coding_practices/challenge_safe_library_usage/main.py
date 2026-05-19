# requirements.txt content (for documentation purposes)
# pandas-datareader==0.10.0
# seaborn==0.13.2

"""
To ensure safe library usage:
- Pin exact versions of all third-party libraries in requirements.txt.
- Regularly check for known vulnerabilities in pinned versions using trusted sources such as the PyPI Security Advisories (https://pypi.org/security/) or the Python Packaging Advisory Database (https://github.com/pypa/advisory-db).
- Update pinned versions as soon as security patches are released.
"""

import pandas_datareader as pdr  # Version pinned: pandas-datareader==0.10.0
import seaborn as sns  # Version pinned: seaborn==0.13.2
import datetime

def fetch_financial_data(symbol, start, end):
    # Fetch stock data from Yahoo Finance using a pinned version of pandas-datareader
    data = pdr.DataReader(symbol, "yahoo", start, end)
    return data

def plot_data(data):
    # Plot the 'Close' prices using a pinned version of seaborn
    sns.lineplot(data=data['Close'])

start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
# For demonstration only; comment out actual data fetching/plotting if needed for offline tests
# stock_data = fetch_financial_data('AAPL', start_date, end_date)
# plot_data(stock_data)
