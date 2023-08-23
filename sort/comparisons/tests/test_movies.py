import pytest
from movies import Movie, MovieSorter

@pytest.fixture
def sample_movies():
    return [
        Movie("Meet the Killer Parents", 2023, ["Thriller"]),
        Movie("Transformers: Rise of the Beasts", 2023, ["Action", "Adventure", "Sci-Fi"]),
        Movie("F9: The Fast Saga", 2021, ["Action", "Crime", "Thriller"]),
        Movie("Avatar: The Way of Water", 2022, ["Action", "Adventure", "Fantasy"]),
        Movie("Top Gun: Maverick", 2022, ["Action", "Drama"]),
        Movie("Frozen", 2013, ["Animation", "Adventure", "Comedy"]),

    ]

def test_sort_by_recent_year_first(sample_movies):
    sorter = MovieSorter()
    movies_sorted = sorted(sample_movies, key=sorter.sort_by_recent_year_first, reverse=True)
    expected_titles = [
        "Meet the Killer Parents",
        "Transformers: Rise of the Beasts",
        "Avatar: The Way of Water",
        "Top Gun: Maverick",
        "F9: The Fast Saga",
        "Frozen",
    ]
    assert [movie.title for movie in movies_sorted] == expected_titles

def test_sort_alphabetically_by_title(sample_movies):
    sorter = MovieSorter()
    movies_sorted = sorted(sample_movies, key=sorter.sort_alphabetically_by_title)
    expected_titles = [
        "Avatar: The Way of Water",
        "F9: The Fast Saga",
        "Frozen",
        "Meet the Killer Parents",
        "Top Gun: Maverick",
        "Transformers: Rise of the Beasts",
    ]
    assert [movie.title for movie in movies_sorted] == expected_titles