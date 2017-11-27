import webbrowser


class Movie():
    # Class description
    """This class provides a way to store movies"""

    # Movie Ratings
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'PG-16', 'R18']

    # Class instance constructor
    def __init__(self, m_title, m_storyline, poster_image, trailer_link):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link

    # Function to open movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
