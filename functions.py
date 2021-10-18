def count_genre(genres, dataframe):
    result = []
    for genre in genres:
        count = dataframe[genre].value_counts()[1]
        result.append(count)
    
    return result