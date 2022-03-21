import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import missingno as msno
#Para ver los NAN values de una forma mas amigable

if __name__=="__main__":
    df = pd.read_csv("mobiles.csv")
    df['count'] = 1

    #Brand with most product offerings for the Indian Market
    """ brands = df.groupby("Brand").sum().sort_values('count', ascending=False)['count']
    b = df['Brand'].value_counts()

    fig, ax = plt.subplots()

    sns.barplot(brands.index, b.values, ax=ax)

    ax.set_title("Offer products by brands")

    ax.set_xlabel("Brands")

    ax.set_ylabel("Quantity")

    plt.show() """

    #Most common specs offered by various brands (eg. if 4 GB memory and 64GB storage models are more commonly offered by all brands)

    """ common_specs = df.groupby(['Brand','Memory','Storage']).sum()

    g = common_specs['count'].groupby('Brand', group_keys=False).nlargest(3)

    print(type(g)) """

    #Most commonly offered colors by all Brands
    
    """ common_colors = df['Color'].value_counts()[:5]

    plt.style.use('ggplot')

    fig, ax = plt.subplots()

    sns.barplot(common_colors.index, common_colors.values, ax = ax)

    ax.set_title('Most 5 common colors')

    ax.set_xlabel('Colors')

    ax.set_ylabel('Quantity')

    plt.show() """

    fig, ax = plt.subplots()
    #sns.stripplot(y="Rating", x="Brand", data=df, ax= ax)
    #sns.boxplot(y="Rating", x="Brand", data=df, ax= ax)
    #sns.countplot(x="Brand", data=df)

    plt.show()