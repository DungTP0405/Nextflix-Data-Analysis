# -*- coding: utf-8 -*-
"""Porfolio_Netflix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cXURX2cvZ_oJKCjk8N3NPZlDaBe7eJ5b
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/content/netflix_titles.csv')
df

df.info()

df.describe()

"""## **Top 5 Directors with The Most Netflix Films: 1943–2020**"""

director_exploded = df[['show_id', 'director']]
director_exploded = director_exploded.assign(director = director_exploded['director'].str.split(',')).explode('director')
director_exploded['director'] = director_exploded['director'].str.strip()
director_exploded = director_exploded.dropna().groupby('director').count().sort_values('show_id', ascending= False).head(5)
director_exploded = director_exploded.rename({'show_id':'shows'})
director_exploded

director_exploded.plot(kind='barh', figsize=(10, 5))
plt.xlabel('Number of Shows')
plt.ylabel('Director')
plt.title('Top 5 Directors with the Most Shows on Netflix')
plt.show()

"""## **Top 5 Actors with The Most Netflix Shows: 1943–2020**"""

cast_exploded = df[['show_id', 'cast']]
cast_exploded = cast_exploded.assign(cast = cast_exploded['cast'].str.split(',')).explode('cast')
cast_exploded['cast'] = cast_exploded['cast'].str.strip()
cast_exploded = cast_exploded.dropna().groupby('cast').count().sort_values('show_id', ascending = False).head(5)
cast_exploded = cast_exploded.rename(columns= {'show_id':'shows'})
cast_exploded

cast_exploded['shows'].plot(kind='barh', figsize=(10, 5))
plt.xlabel('Number of Shows')
plt.ylabel('Actor')
plt.title('Top 5 Actors with the Most Shows on Netflix')
plt.show()

"""## **Changes in Netflix's Content Types Over The Years**

"""

type_by_year = df.groupby(['release_year', 'type']).size().reset_index(name = 'numbers')
Movie = type_by_year[(type_by_year['type']== 'Movie') & (type_by_year['release_year'] >= 2010)]
TV_show = type_by_year[(type_by_year['type'] == 'TV Show') & (type_by_year['release_year'] >= 2010)]

Movie

TV_show

plt.plot(Movie['release_year'], Movie['numbers'], label='Movie', color='blue')
plt.plot(TV_show['release_year'], TV_show['numbers'], label='TV Shows', color='orange')
plt.title('Number of shows over years')
plt.xlabel('Year')
plt.ylabel('Number of shows')
plt.legend(title='Type')