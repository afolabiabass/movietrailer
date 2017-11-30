import fresh_tomatoes
import media


# Create Movie Object instance Toy Story
toy_story = media.Movie(
    'Toy Story',
    'Toys come to life',
    'http://www.impawards.com/1995/posters/toy_story_ver1.jpg',
    'https://www.youtube.com/watch?v=SgoiKLFBA3Q')

# Create Movie Object instance Thor Ragnarok
thor_ragnarok = media.Movie(
    'Thor Ragnarok',
    'A fantatsy movie on the comic Thor',
    'http://grandentertainment.ro/sites/default/files/'
    '100925-thor-3-print-poster-a1-payoff-no-imax-compres.jpg',
    'https://www.youtube.com/watch?v=ue80QwXMRHg')

# Create Movie Object instance Xmen
xmen = media.Movie(
    'X-Men',
    'Mutant Humans and Conflict',
    'https://vignette.wikia.nocookie.net/xmenevo/images/0'
    '/03/X-Men_%28Movie%29.jpg/revision/latest?cb=20150405091121',
    'https://www.youtube.com/watch?v=nbNcULQFojc')

# Create Movie Object instance Avengers
avengers = media.Movie(
    'The Avengers',
    'Earths mightiest heroes must come together',
    'https://vignette.wikia.nocookie.net/marvelheroes/images'
    '/9/98/Avengers-movie-poster-1.jpg/revision/latest?cb=20170713041606',
    'https://www.youtube.com/watch?v=eOrNdBpGMv8')

# Create Movie Object instance Guardians of the Galaxy
guardians = media.Movie(
    'Guardians of the Galaxy',
    'Movie about a group of intergalactic criminals',
    'http://i.imgur.com/MdXm6EE.jpg',
    'https://www.youtube.com/watch?v=d96cjJhvlMA')

# Create Movie Object instance Deadpool
deadpool = media.Movie(
    'Deadpool',
    'Movie about a mercenary with a morbid sense of humor',
    'https://ewedit.files.wordpress.com/2015/12/deadpool-poster.jpg',
    'https://www.youtube.com/watch?v=Xithigfg7dA')

# Create list of movie object
movies = [toy_story, thor_ragnarok, xmen, avengers, guardians, deadpool]

# Call fresh tomatoes function open_movies_page and pass movie array
fresh_tomatoes.open_movies_page(movies)
