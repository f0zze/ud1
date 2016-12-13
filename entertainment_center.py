from media import Movie
from helper.fresh_tomatoes import open_movies_page

movies = [
    Movie('The Terminator',
          'https://youtu.be/EpdAcA6ziiA',
          'https://i.jeded.com/i/the-terminator-1984.11880.jpg'),

    Movie('Terminator 2: Judgment Day',
          'https://youtu.be/lwSysg9o7wE',
          'https://goo.gl/08EQkP'),

    Movie('Terminator 3: Rise of the Machines',
          'https://youtu.be/WeC-lGnajT0',
          'https://goo.gl/VtYzRl')
]

# Uses list of movie instances as input to generate an HTML file
# and open it in the browser.
open_movies_page(movies)
