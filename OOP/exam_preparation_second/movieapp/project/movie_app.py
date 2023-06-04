from user import User
from movie_specification.action import Action
from movie_specification.fantasy import Fantasy
from movie_specification.thriller import Thriller


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def find_user_by_username(self, username):
        return next(filter(lambda user: user.username == username, self.users_collection), None)

    def register_user(self, username: str, age: int):
        user = self.find_user_by_username(username)
        if user:
            raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie):
        user = self.find_user_by_username(username)
        if not user:
            raise Exception("This user does not exist!")
        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs):
        user = self.find_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            if key == 'year':
                movie.year = value
            if key == 'age_restriction':
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie):
        user = self.find_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in user.movies_owned:
            user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie):
        user = self.find_user_by_username(username)
        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):
        user = self.find_user_by_username(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        movies_list = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = []
        for movie in movies_list:
            result.append(movie.details())
        return '\n'.join(result)

    def __str__(self):
        result = []
        if not self.users_collection:
            result.append('All users: No users.')
        else:
            start = 'All users: '
            usernames = []
            for user in self.users_collection:
                usernames.append(user.username)
            usernames = ', '.join(usernames)
            end = start + usernames
            result.append(end)
        if not self.movies_collection:
            result.append('All movies: No movies.')
        else:
            movie_titles = []
            start_movie = 'All movies: '
            for movie in self.movies_collection:
                movie_titles.append(movie.title)
            movie_titles = ', '.join(movie_titles)
            end = start_movie + movie_titles
            result.append(end)
        return '\n'.join(result)
