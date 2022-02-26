from email import header
from tkinter.font import names
import pandas as pd

if __name__=="__main__":
    #names significa nombre de las columnas
    df = pd.read_csv('./btc-market-price.csv', header=None, na_values=['','?','-'],
                    names=['Timestamp', 'Price'])
    print(df.head())