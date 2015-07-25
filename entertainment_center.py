# The movie list generator module:
#    will be used by open_movies_page()

from media import Movie
import fresh_tomatoes


def generate_movie_list():

    """
    Create a list of Movie objects and return the list
    """
    movie_list = []
    movie_list.append(
        Movie('Toy Story 3',
              'Lee Unkrich',
              ' June 18, 2010',
              './toy_story_3.jpg',
              'https://www.youtube.com/watch?v=JcpWXaA2qeg')
    )
    movie_list.append(
        Movie('School of Rock',
              'Richard Linklater',
              'October 3, 2003',
              'school_of_rock.jpg',
              'https://youtu.be/3PsUJFEBC74')
    )
    movie_list.append(
        Movie('Ratatouille',
              'Brad Bird, Jan Pinkava',
              'June 29, 2007',
              'RatatouillePoster.jpg',
              'https://youtu.be/uVeNEbh3A4U')
    )

    return movie_list

fresh_tomatoes.open_movies_page(generate_movie_list())
