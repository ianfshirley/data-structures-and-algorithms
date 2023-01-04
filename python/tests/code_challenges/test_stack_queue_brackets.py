import pytest
from code_challenges.stack_queue_brackets import multi_bracket_validation


# @pytest.mark.skip("TODO")
def test_validates_two_square_brackets():
    actual = multi_bracket_validation("[]")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_square_brackets_flipped():
    actual = multi_bracket_validation("][")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_validates_two_braces():
    actual = multi_bracket_validation("{}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_braces_flipped():
    actual = multi_bracket_validation("}{")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_validates_two_parentheses():
    actual = multi_bracket_validation("()")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_parentheses_flipped():
    actual = multi_bracket_validation(")(")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_multi():
    actual = multi_bracket_validation("{}(){}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_nested():
    actual = multi_bracket_validation("{([])}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_mismatched():
    actual = multi_bracket_validation("[}")
    expected = False
    assert actual == expected


def test_your_mom():
    actual = multi_bracket_validation("[your mom}")
    expected = False
    assert actual == expected


def test_my_mom_with_brackets():
    actual = multi_bracket_validation("[my[ mom}")
    expected = False
    assert actual == expected


def test_code_fellows():
    actual = multi_bracket_validation("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected


def test_extra_characters():
    actual = multi_bracket_validation("()[[Extra Characters]]")
    expected = True
    assert actual == expected

