import pytest
from code_challenges.movies import movies, sort_by_title, sort_by_year


# # Expected test output of test #1
# expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# # Expected test output of test #2
# expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]


def test_sort_by_title():
  actual = sort_by_title(movies)
  expected = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]
  assert actual == expected


def test_sort_by_year():
  actual = sort_by_year(movies)
  expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]