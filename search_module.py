import os
from forms import SearchForm
from flask import render_template



# SEARCH MODULE
def search(search_term, username):
    
    searchform = SearchForm()
    search_results = []
    series_search_results = {}
    
    search_results = CharacterSearchResults(search_term, search_results)
    character_search_results = search_results.return_characters(
        search_term, search_results)
    
    series_search_results = SeriesSearchResults(
        search_term, series_search_results)
    series_search_results = series_search_results.return_series(
        search_term, series_search_results)
    
    
    nav_image_src = "/static/images/marvel-logo.webp"
    
    return render_template('/content/characters/display_search_results.html', character_search_results=character_search_results,
    series_search_results=series_search_results,nav_image_src=nav_image_src, username=username, searchform=searchform)


class CharacterSearchResults:
    def __init__(self, search_term: str, search_results: list) -> None:
        self.search_term = search_term
        self.search_results = search_results

    def return_characters(self, search_term, search_results: list) -> list:

        title_search_term = search_term.title()

        search_term = title_search_term.strip()

        directory = 'character_misspellings/misspelling_files'
        search_results = []

        for filename in os.listdir(directory):
            f = open(f'{directory}/{filename}', 'r')
            content = f.read()
            lines = content.splitlines()
            for line in lines:
                if search_term in line:
                    corrected_name = filename.removesuffix('.txt')
                    if corrected_name not in search_results:
                        search_results.append(corrected_name)
        return search_results

    @classmethod
    def search_results(cls, search_term, search_results):
        return cls(search_term=search_term, search_results=search_results)


class SeriesSearchResults:
    def __init__(self, search_term: str, series_search_results: dict) -> None:
        self.search_term = search_term
        self.search_results = series_search_results

    def return_series(self, search_term, series_search_results: dict) -> dict:

        title_search_term = search_term.title()

        search_term = title_search_term.strip()

        directory = 'series_names/series_names_files'
        series_search_results = {}

        for filename in os.listdir(directory):
            f = open(f'{directory}/{filename}', 'r')
            content = f.read()

            l = open(f'{directory}/{filename}', 'r')
            first_line = l.readline()
            series_name = first_line.removesuffix('\n')

            series_id = filename.removesuffix('.txt')

            split_terms = search_term.split()

            for term in split_terms:
                if term in content:
                    series_search_results[series_id] = series_name
        return series_search_results

    @classmethod
    def search_results(cls, search_term, series_search_results):
        return cls(search_term=search_term, series_search_results=series_search_results)
