# Movie_trailer: a movie trailer display site

## Quick Start for Users

- Please check out the project

```
$git clone https://github.com/syang/movie_trailer.git
```

- Enter the project directory

```
$cd movie_trailer
```

- Invoke the program as follows

```
$python entertainment_center.py
```

## Code Structure for Readers/Developers

    * fresh_tomatoes.py  - the site generation module, containing functions that generate movie trailer pages
    * media.py  - the data structure module, describing what fields/data a movie contains
    * entertainment_center.py - this is the module that create a list of movies

#### Code style checking
Note that: we don't fix code styple problems in the fresh_tomatoes.py module

```
$pip install -r requirements.txt
$flake8 *.py
```
