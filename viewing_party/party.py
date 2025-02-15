import copy
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        new_movie = None
        return new_movie
    
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    copied_data = copy.deepcopy(user_data["watchlist"])

    for movie in copied_data:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    average_rating = 0.0

    if user_data["watched"]:
        for movie in user_data["watched"]:
            average_rating += movie["rating"]
    else:
        return average_rating

    return average_rating / len(user_data["watched"])


def get_most_watched_genre(user_data):
    genre_frequency = {}

    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_frequency:
            genre_frequency[movie["genre"]] = 1
        else:
            genre_frequency[movie["genre"]] += 1

    max_value = max(genre_frequency.values())

    for genre, value in genre_frequency.items():
        if value == max_value:
            return genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_movies = []
    user_unique_watched = []

    for friend in user_data["friends"]:
        for fr_movie in friend["watched"]:
            if fr_movie not in friends_movies:
                friends_movies.append(fr_movie)

    for user_movie in user_data["watched"]:
        if user_movie not in friends_movies:
            user_unique_watched.append(user_movie)

    return user_unique_watched


def get_friends_unique_watched(user_data):
    friends_movies = []
    fr_unique_movies = []

    for friends in user_data["friends"]:
        for fr_movie in friends["watched"]:
            if fr_movie not in friends_movies:
                friends_movies.append(fr_movie)

    user_movies = user_data["watched"]

    for fr_movie in friends_movies:
        if fr_movie not in user_movies:
            fr_unique_movies.append(fr_movie)

    return fr_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    unique_movies = get_friends_unique_watched(user_data)

    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []

    friends_watched_movies = get_friends_unique_watched(user_data)
    frequent_genre = get_most_watched_genre(user_data)

    for movie in friends_watched_movies:
        if movie["genre"] == frequent_genre:
            recommended_movies.append(movie)

    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []

    user_watched_unique_movies = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in user_watched_unique_movies:
            recommended_movies.append(movie)

    return recommended_movies

