import pytest
from code_challenges.merge_sort import merge_sort


def test_merge_sort():
  example_list = [38, 27, 43, 3, 9, 82, 10]
  actual = merge_sort(example_list)
  expected = [3, 9, 10, 27, 38, 43, 82]