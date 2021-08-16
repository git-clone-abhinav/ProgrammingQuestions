# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    if text == "":
        return ""
    else:
        if "-" in text:
            text = text.strip().split("-")
        if " " in text:
            text = text.strip().split(" ")
        if "_" in text:
            text = text.strip().split("_")
        sent = text[0]
        for word in text[1:]:
            sent = sent + word.capitalize()
        return sent