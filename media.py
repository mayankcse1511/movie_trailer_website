# importing the webbrowser module
import webbrowser
# making a class movie for the movie data


class Movie():
    """ this class provides a way to store movie relaed information"""
    # it is a constructor which is called whenever the class Movie is called
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
