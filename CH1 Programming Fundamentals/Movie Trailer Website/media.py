class Movie():
    """ 

    This class provides a way to store movie related information

    Attributes:
    movie_title (str): Title of the movie
    movie_storyline (str): Storyline of the movie
    poster_image (str): Image of the movie
    trailer_youtube (str): Trailer of the movie

    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Init Movie with title, storyline, poster image, and trailer """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
