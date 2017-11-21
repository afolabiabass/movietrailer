import webbrowser

class Movie():
    """ This class provides a way to store movies """
    
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'PG-16', 'R18']

    ##Class instance constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    ##Function to open movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
