#!/usr/bin/python3

"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """
    Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    txt = text[:]
    for p in ".?:":
        list_text = txt.split(p)
        txt = ""
        for i in list_text:
            i = i.strip(" ")
            txt = i + p if txt == "" else txt + "\n\n" + i + p

    print(txt[:-3], end="")
