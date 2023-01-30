import pytest
from data_structures.hashtable import Hashtable


# @pytest.mark.skip("TODO")
def test_exists():
    assert Hashtable


# Successfully hash a key to an in-range value
# @pytest.mark.skip("TODO")
def test_hash():
    hashtable = Hashtable()
    actual = hashtable._hash("squid")
    expected = 746
    assert actual == expected


# Setting a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored
# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_has():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.has("listen")
    expected = True
    assert actual == expected


# Successfully returns an error message for a key that does not exist in the hashtable
# @pytest.mark.skip("TODO")
def test_has_none():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.has("ian")
    expected = False
    assert actual == expected


# Successfully returns a list of all unique keys that exist in the hashtable
# @pytest.mark.skip("TODO")
def test_keys():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.keys()
    expected = ["ahmad", "listen", "silent"]
    assert actual == expected


# Successfully handle a collision within the hashtable
# @pytest.mark.skip("TODO")
# def test_collision():
#     hashtable = Hashtable(10)
#     hashtable.set("god", "god")
#     hashtable.set("dog", "dog")
#     index = hashtable._hash("god")

    # expected = hashtable._hash("dog")
    # assert actual == expected

# Successfully retrieve a value from a bucket within the hashtable that has a collision
@pytest.mark.skip("TODO")
def test_collision_retrieve_value():
    pass


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
