from requests import get
import re


url = ""


def get_words():
    return (get(url).text).split("\n")


def check_word(sentence):
    words = get_words()
    for i in sentence:
        for j in words:
            if i.lower() == j.lower():
                return j, True  # re
    return None, False
