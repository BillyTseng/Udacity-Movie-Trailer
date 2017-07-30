import webbrowser


class Movie():
    def __init__(
        self, movie_title, movie_storyline, poster_imgae, trailer_youtube
    ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_imgae
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
