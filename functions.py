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
