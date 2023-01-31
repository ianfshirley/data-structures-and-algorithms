from data_structures.hashtable import Hashtable
import re


def first_repeated_word(str):
    words = [re.sub(r'[^\w\s]', '', word).lower() for word in str.split()]
    word_set = set()
    for word in words:
        if word in word_set:
            return word
        word_set.add(word)
    return