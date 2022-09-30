
import pandas as pd
def getting_recommended_movie(moviename):
    df_kwds=pd.read_csv('data/cosine_similarity.gzip',compression='gzip',index_col='Title')
    df_kwds=df_kwds.sort_values(by=moviename,ascending=False)[[moviename]].head(6)
    #print(df_kwds)
    df_new =df_kwds.copy()
    
    #print(type(df_new))
    df_new['SearchType']="KB"
    df_user_rev=pd.read_csv('data/user_review_similarity.gzip',compression='gzip',index_col='Title')
    df_user_rev=df_user_rev.sort_values(by=moviename,ascending=False)[[moviename]].head(6)
    df_user_rev['SearchType']="UR"
    #print(df_user_rev)
    df_new =df_new.append(df_user_rev)
    df_new.drop(columns=[moviename],inplace=True)
    return df_new
if __name__ == "__main__":
    print(getting_recommended_movie("American Beauty (1999)"))