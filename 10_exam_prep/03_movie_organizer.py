def movie_organizer(*args):
    movies = {}

    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    for genre, movies_list in movies.items():
        movies_list.sort()

    sorted_genres = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for genre, movies_list in sorted_genres:
        result += f"{genre} - {len(movies_list)}\n"
        for movie in movies_list:
            result += f"* {movie}\n"

    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
