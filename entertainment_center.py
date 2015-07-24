# The movie list generator module:
#    will be used by open_movies_page()

from media import Movie


def generate_movie_list():

    """
    Create a list of Movie objects and return the list
    """
    movie_list = []
    movie_list.append(
        Movie('Toy Story 3',
              './toy_story_3.jpg',
              'https://www.youtube.com/watch?v=JcpWXaA2qeg')
    )
    movie_list.append(
        Movie('School of Rock',
              'school_of_rock.jpg',
              'https://youtu.be/3PsUJFEBC74')
    )
    movie_list.append(
        Movie('Ratatouille',
              'RatatouillePoster.jpg',
              'https://youtu.be/uVeNEbh3A4U')
    )

    return movie_list
