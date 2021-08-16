# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def getCount(sentence):
    count = 0 # temporary variable
    for char in sentence: # character iterator
        if char in "aeiou":
            count += 1 # count incrementor
            
    return count

def getCount(sentence):
    return sum(c in 'aeiou' for c in sentence)

def getCount(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")