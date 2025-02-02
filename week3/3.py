movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#1
def rate(movie):
    return movie["imdb"] > 5.5

#2
def high_movie(movies):
    return [movie for movie in movies if high_movie(movies)]

#3
def category(mov,cat):
    return [movie for movie in movies if movie["category"]==cat]

#4
def average(mov):
    return sum(movie["imdb"] for movie in mov)/ len(mov) if mov else 0

#5
def score(mov,cat):
    category= category(mov,cat)
    return average(category)

print(rate(movies[0]))
print(high_movie(movies))
print(category(movies, "Romance"))
print(average(movies))
print(score(movies, "Romance"))