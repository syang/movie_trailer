class Movie:
    """ This class contains the data that describes a movie

    __init__(self, title, poster_image_url, trailer_youtube_url)
    Parameters:
        title: the title of movie
        poster_image_url: the url of the poster_image_url
        trailer_youtube_url: the url of youtube trailer

    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
