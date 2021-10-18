
def get_movie_colum_names():
    movie_colum_names=["movie_id","movie_title","release_date","video_release_date",
    "IMDb_URL","unknown","Action","Adventure","Animation",
    "Children","Comedy","Crime","Documentary","Drama","Fantasy",
    "Film_Noir","Horror","Musical","Mystery","Romance","Sci-Fi",
    "Thriller","War","Western"]

    return movie_colum_names

def get_rating_colum_names():
    rating_colum_names=["user_id","movie_id","rating","timestamp"]

    return rating_colum_names

def get_user_colum_names():
    user_column_names = ["user_id","age","gender","occupation","zip_code"]

    return user_column_names