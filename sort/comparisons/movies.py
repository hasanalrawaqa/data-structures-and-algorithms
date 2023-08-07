class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres


class MovieSorter:
    @staticmethod
    def sort_by_recent_year_first(movie):
        return movie.year

    @staticmethod
    def sort_alphabetically_by_title(movie):
        def remove_leading_articles(title):
            leading_articles = ["A ", "An ", "The "]
            for article in leading_articles:
                if title.startswith(article):
                    return title[len(article):]
            return title

        return remove_leading_articles(movie.title.lower())
