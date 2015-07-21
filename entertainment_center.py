from media import Movie


def generate_movie_list():

    """
    Create a list of Movie objects and return the list
    """
    movie_list = []
    movie_list.append(
        Movie('Toy Story 3',
              'http://www.gstatic.com/tv/thumb/dvdboxart/\
              3546307/p3546307_d_v7_aa.jpg',
              'https://www.youtube.com/watch?v=JcpWXaA2qeg')
    )
    movie_list.append(
        Movie('School of Rock',
              'https://upload.wikimedia.org/wikipedia/en/\
              1/11/School_of_Rock_Poster.jpg',
              'https://youtu.be/3PsUJFEBC74')
    )
    movie_list.append(
        Movie('Ratatouille',
              'https://upload.wikimedia.org/wikipedia/\
              en/5/50/RatatouillePoster.jpg',
              'https://youtu.be/uVeNEbh3A4U')
    )

    return movie_list
