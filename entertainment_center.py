from media import Movie
from helper.fresh_tomatoes import open_movies_page

movies = [
    Movie('The Terminator',
          'https://youtu.be/EpdAcA6ziiA',
          'https://i.jeded.com/i/the-terminator-1984.11880.jpg'),

    Movie('Terminator 2: Judgment Day',
          'https://youtu.be/lwSysg9o7wE',
          'http://manapop.com/wp-content/uploads/2014/06/terminator-2-judgment-day-52465043d262c.jpg'),

    Movie('Terminator 3: Rise of the Machines',
          'https://youtu.be/WeC-lGnajT0',
          'http://vignette4.wikia.nocookie.net/terminator/images/3/3f/600full-terminator-3_-rise-of-the-machines-poster_T-X.jpg/revision/latest?cb=20120312033325')
]


open_movies_page(movies)
