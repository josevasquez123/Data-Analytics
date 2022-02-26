from calendar import month
from tkinter import VERTICAL
import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    df = pd.read_csv('btc-market-price.csv', header=None, names=['Time', 'Price'], na_values=['','-','?'],dtype={'Price':'float'})

    df = df.dropna()

    df['Time'] = pd.to_datetime(df['Time'])

    df['Month'] = df['Time'].dt.month

    result_max = df.groupby('Month').max()

    result_min = df.groupby('Month').min()

    months = ['Jan', 'Feb', 'March', 'April','May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.bar(months, result_min['Price'])

    ax2.bar(months, result_max['Price'])

    plt.show()


    """ plt.bar(months, result_max['Price'])

    plt.xticks(months, rotation='vertical')

    plt.ylabel('Price ($)')

    plt.xlabel('Months')

    plt.title('BTC max value/month')

    plt.show()

    print(result) """