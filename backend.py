import pickle

movie_list = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))


def get_recommendation(movie):
    index = movie_list[movie_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [movie_list.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies


