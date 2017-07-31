import media
import fresh_tomatoes

# The dataset of movies ---Start---
star_wars7 = media.Movie(
    "Star Wars: The Force Awakens",
    "The Force Awakens is the first installment of the Star Wars trilogy",
    "https://goo.gl/TsKrkR",
    "https://www.youtube.com/watch?v=sGbxmsDFVnE"
)

kingsman2 = media.Movie(
    "Kingsman: The Golden Circle",
    "Kingsman: is an upcoming British-American action comedy spy film",
    "https://goo.gl/uL6TTZ",
    "https://www.youtube.com/watch?v=0fvqnGmr9S8"
)

the_intern = media.Movie(
    "The Intern",
    "Ben Whittaker applies to a senior citizen intern program",
    "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
    "https://www.youtube.com/watch?v=ZU3Xban0Y6A"
)
# The dataset of movies ---End---

# group all the instances together in a list
movies = [star_wars7, kingsman2, the_intern]

# Call the method of fresh_tomatoes.py to render the movie trailer webpage.
fresh_tomatoes.open_movies_page(movies)
