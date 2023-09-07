#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    txt = text[:]
    for p in ".?:":
        list_text = txt.split(p)
        txt = ""
        for i in list_text:
            i = i.strip(" ")
            txt = i + p if txt is "" else txt + "\n\n" + i + p

    print(txt[:-3], end="")
