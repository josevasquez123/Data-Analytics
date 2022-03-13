import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i-0.1,y[i]+5,y[i], fontweight='bold')

if __name__=="__main__":
    df = pd.read_csv("netflix_titles.csv")

    df['count'] = 1

    #Top ratings
    """ 

    ratings = df.groupby('rating').sum().reset_index()

    ratings = ratings.sort_values(by='count', ascending=False)

    ratings_cat = ratings['rating']

    rating_quantity = ratings['count']

    plt.style.use('seaborn-whitegrid')

    plt.bar(ratings_cat, rating_quantity)

    #addlabels(ratings_cat, rating_quantity)

    plt.title('Rating')

    plt.ylabel('Total Rating', fontweight='bold', fontsize=13)

    plt.xlabel('Rating Name', fontweight='bold', fontsize=13)

    plt.show() """

    #Top countries with highest number of movies realized

    """ df = df[~df['country'].isna()]

    top_country = df.groupby(['type', 'country']).sum().reset_index()

    top_country = top_country.sort_values(by='count', ascending=False)

    top_country = top_country[top_country['type']=='Movie'][:10].reset_index()

    country_names = top_country['country']
    number_movies = top_country['count']

    plt.pie(number_movies, labels=country_names, autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(number_movies)/100)
            ,textprops={'fontsize':7}, startangle=45)

    plt.legend(loc='lower left')

    plt.show() """

    #Month with highest movies, Tv added to netflix

    df['date_added'] = pd.to_datetime(df['date_added'])

    df['month_added'] = df['date_added'].dt.month

    df = df[~df['month_added'].isna()]

    df['month_added'] = df['month_added'].astype('int32')

    highest_months = df.groupby('month_added').sum()
    highest_months = highest_months.sort_values(by='count',ascending=False).reset_index()

    months = highest_months['month_added']

    quantity = highest_months['count']
    
    ax = plt.bar(months, quantity)

    c1 = mplcursors.cursor(ax, hover=mplcursors.HoverMode.Transient)

    @c1.connect("add")

    def _(sel):
        sel.annotation.set_text(
        f'Movies: {highest_months["count"][sel.index]}\nMonth: {highest_months["month_added"][sel.index]}')
        sel.annotation.get_bbox_patch().set(fc="white")
        sel.annotation.arrow_patch.set(fc="black", alpha=.7)

    plt.show()





    

    