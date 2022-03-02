from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":

    column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

    df = pd.read_csv("movies.csv", delimiter="|", header=None, na_values=['?'], names=column_names, thousands=',')
    df = df.dropna()

    #Show in a bar chart the 5 longer movies

    """ df = df.sort_values('duration', ascending=False)

    longer_movies = df['movie_title'][:5]

    durations = df['duration'][:5]

    x = np.arange(len(longer_movies))

    plt.bar(x, durations)

    plt.title('5 longer movies')

    plt.ylabel('Duration (minuts)')

    plt.xlabel('Movie name', color='red')

    plt.xticks(x, longer_movies, fontsize='8')

    plt.grid()

    plt.show() """

    #Best movies by year

    """ groups = df.groupby('title_year')

    max_score_by_year = df.groupby('title_year')['imdb_score'].max()

    x = np.arange(len(max_score_by_year))

    plt.bar(x, max_score_by_year)

    plt.title('Best movies by year')

    plt.ylabel('Score')

    plt.xlabel('Movie year', color='red')

    plt.xticks(x, max_score_by_year.index, fontsize='8')

    plt.grid()

    plt.show() """

    #Action movie with higher critics

    action_groups = df.groupby('genre').get_group('Action')

    higher = action_groups.loc[action_groups['num_critic_for_reviews'].idxmax]

    print(higher)

    print(f'Movie: {higher["movie_title"]}, score: {higher["num_critic_for_reviews"]}')



    

