import pandas as pd
from column_names import get_movie_colum_names, get_rating_colum_names, get_user_colum_names

def get_all_data():
    
    enconding = "ISO-8859-1"
    movie_file = "./ml-100k/u.item"
    rating_file = "./ml-100k/u.data"
    user_file = "./ml-100k/u.user"

    data_movie = pd.read_csv(movie_file, encoding='ISO-8859-1',
                            sep="|", names=get_movie_colum_names())

    data_rating = pd.read_csv(rating_file, encoding='ISO-8859-1',
                            sep="\t", names=get_rating_colum_names())

    data_user = pd.read_csv(user_file, encoding='ISO-8859-1',
                        sep="|", names=get_user_colum_names())

    return [data_movie, data_rating, data_user]

def count_genre(genres, dataframe):
    result = []
    for genre in genres:
        count = dataframe[genre].value_counts()[1]
        result.append(count)
    
    return result

def data_result_all_years_by_gender(data, gender):
    data_result = data.loc[data.gender == gender] \
        .groupby(data.release_date.dt.year).size()\
            .reset_index(name="times")
    
    return data_result

def data_result_by_set_of_years_by_gender(data, gender, years):
    data_result = data.loc[(data.gender == gender) & data.release_date.dt.year.isin(years)]\
        .groupby(data.release_date.dt.year).size()\
            .reset_index(name="times")
    
    return data_result
