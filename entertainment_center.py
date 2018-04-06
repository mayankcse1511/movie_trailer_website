# imported the file fresh_tomatoes.py
import fresh_tomatoes

# imported the file media.py
import media

# below are the instances of class Movie which is in the module media.py
padmaavat = media.Movie("padmavat",
                        "a story of honor, valor and obsession",
                        "https://upload.wikimedia.org/wikipedia/en"
                        "/7/73/Padmaavat_poster.jpg",
                        "https://www.youtube.com/watch?v=X_5_BLt76c0&t=83s")
spdrmn_hmecmng = media.Movie("Spider Man Homecoming",
                             " the story of superhero spiderman",
                             "https://upload.wikimedia.org/wikipedia/en"
                             "/f/f9/Spider-Man_Homecoming_poster.jpg",
                             "https://www.youtube.com/watch?v=U0D3AOldjMU")
dadpol = media.Movie("Deadpool", " the story of superhero deadpool",
                     "https://upload.wikimedia.org/wikipedia/en/"
                     "4/46/Deadpool_poster.jpg",
                     "https://www.youtube.com/watch?v=xZNBFcwd7zc")
hngvr = media.Movie("Hangover", " story of 3 boys who can't handle vegas",
                    "https://upload.wikimedia.org/wikipedia/en/b"
                    "/b9/Hangoverposter09.jpg",
                    "https://www.youtube.com/watch?v=vhFVZsk3XEs")
Th_intrnshp = media.Movie("The Internship",
                          " the story of 2 persons who lost their jobs",
                          "https://upload.wikimedia.org/wikipedia/en"
                          "/e/ed/The-internship-poster.jpg",
                          "https://www.youtube.com/watch?v=cdnoqCViqUo")
th_rvnnt = media.Movie(" The Revenant ",
                       " man who survives from extreme tough times",
                       "https://upload.wikimedia.org/wikipedia"
                       "/en/b/b6/The_Revenant_2015_film_poster.jpg",
                       "https://www.youtube.com/watch?v=LoebZZ8K5N0")
# the list of the movies is passed to the array of list i.e. movies.
movies = [padmaavat, spdrmn_hmecmng,
          dadpol, hngvr, Th_intrnshp, th_rvnnt]
# list of movies as argument to open_movies_page in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
