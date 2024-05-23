from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)


movie_list = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html', movies=movie_list['title'].values)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie = data.get('movie')
    if not movie:
        return jsonify({"error": "No movie provided"}), 400
    if movie not in movie_list['title'].values:
        return jsonify({"error": "Movie not found"}), 404
    index = movie_list[movie_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = [movie_list.iloc[i[0]].title for i in distances]
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
