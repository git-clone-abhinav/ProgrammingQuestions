# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    t=""
    for letter in word:
        if word.count(letter.lower()) > 1:
            t=t+")"
        else:
            t=t+"("

    return t