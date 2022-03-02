import pandas as pd
import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i-0.1,y[i]+5,y[i], fontweight='bold')

if __name__=="__main__":
    sheets = pd.read_excel("products.xlsx", sheet_name=[0,2])

    sheets[0]['brand'] = sheets[0]['brand'].str.lower()

    sheets[0]['merchant_id'] = sheets[0]['merchant_id'].astype(str)

    id_description = sheets[2]

    id_description['merchant_id'] = id_description['merchant_id'].astype(str)

    #What is the brand with highest sales

    """ brands = sheets[0].groupby('brand').sum()

    highest_sales_brand = brands.loc[brands['price'].idxmax]

    print(f'brand: {highest_sales_brand.name}, sales: {highest_sales_brand["price"]}')  """

    #Show in a barchart the 5 brands with lower sales

    """ brands = sheets[0].groupby('brand').sum()

    brands = brands.sort_values(['price'])

    lower_brand_prices = brands['price'][:5]

    lower_brand_names = lower_brand_prices.index.values

    plt.style.use('seaborn-whitegrid')

    plt.bar(lower_brand_names, lower_brand_prices)

    plt.title("5 lower brands sales")

    plt.ylabel("Sales $")

    plt.xlabel("Brand name")

    plt.show() """

    #Show 5 merchant with highest sales

    merchants = sheets[0].groupby('merchant_id').count()                #Cantidad de productos vendidos agrupados por el vendedor

    x = merchants['name'].nlargest(5)                                   #Los 5 mayores vendedores

    lower_merchants_id = x.index.values                                 #El ID de los vendedores

    sales_quantity = x.values                                           #Su numero de ventas
    
    #Obtener el nombre de los vendedores mediante el ID

    names = []

    for descrip in lower_merchants_id:
        x = id_description[id_description['merchant_id']==descrip]

        names.append(x.iloc[0]['merchant'])           

    plt.style.use('seaborn-whitegrid')

    plt.bar(names, sales_quantity)

    addlabels(names, sales_quantity)

    plt.title("5 highest merchants sales")

    plt.ylabel("Sales Quantity")

    plt.xlabel("Merchant ID")

    plt.show()    



