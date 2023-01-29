import pytest
from code_challenges.merge_sort import merge_sort


def test_merge_sort():
  example_list = [38, 27, 43, 3, 9, 82, 10]
  actual = merge_sort(example_list)
  expected = [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_reversed():
  example_list = [20, 18, 12, 8, 5, -2]
  actual = merge_sort(example_list)
  expected = [-2, 5, 8, 12, 18, 20]


def test_merge_sort_repeats():
  example_list = [5, 12, 7, 5, 5, 7]
  actual = merge_sort(example_list)
  expected = [5, 5, 5, 7, 7, 12]

def test_merge_sort_nearly_sorted():
  example_list = [2, 3, 5, 7, 13, 11]
  actual = merge_sort(example_list)
  expected = [2, 3, 5, 7, 11, 13]


def test_merge_sort_empty():
  example_list = []
  actual = merge_sort(example_list)
  expected = []