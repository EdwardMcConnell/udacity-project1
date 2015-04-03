import webbrowser

class Movie():
    """This class provies a way to store and retrieve movie related information"""

    FAMILY_RATINGS = ['G','PG','PG-13']

    def __init__(self, 
                 movie_title, 
                 poster_image, 
                 youtube_trailer,
                 rating,
                 synopsis,
                 duration,
                 release_date):

        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.rating = rating
        self.synopsis = synopsis
        self.duration = duration
        self.release_date = release_date

    def is_family_friendly(self):
        if self.rating in Movie.FAMILY_RATINGS:
            return True
        else:
            return False

