import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def remove_year(val):
    return val[0 : val.find("(") - 1]


def splitting_gen(val):
    return " " + " ".join([str(elem) for elem in val.split("|")])


# Import the two datasets
movies_df = pd.read_csv('data/movies_df.gzip',compression='gzip')
rating_df = rating_df =pd.read_csv('data/rating_df.gzip',compression='gzip')

movies_df["Search_Criteria"] = movies_df["Title"].apply(remove_year)
movies_df["Search_Criteria"] = movies_df["Search_Criteria"] + movies_df["Genres"].apply(
    splitting_gen
)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies_df["Search_Criteria"])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cos_similarty_df = pd.DataFrame(cosine_sim,columns=movies_df["Title"])
cos_similarty_df.index=movies_df["Title"]
cos_similarty_df.apply(lambda x: round(x,3))
cos_similarty_df=cos_similarty_df.applymap(lambda x: 0 if round(x)==1 else x)
cos_similarty_df.to_csv('data/cosine_similarity.gzip',compression={'method': 'gzip'})

df_user_review = pd.merge(movies_df, rating_df, on='MovieID')
columns =['MovieID','Title','UserID','Rating']
df_user_review = df_user_review[columns]
moviemat = df_user_review.pivot_table(index='UserID', columns='Title', values='Rating')
for item in set(movies_df['Title'].unique()).difference(set(moviemat.columns)):
    moviemat[item]=0
user_review_based_df =moviemat.corr()
user_review_based_df.apply(lambda x: round(x,3))
user_review_based_df.fillna(0,inplace=True)
user_review_based_df=user_review_based_df.applymap(lambda x: 0 if round(x)==1 else x)
user_review_based_df.to_csv('data/user_review_similarity.gzip',compression={'method': 'gzip'})

