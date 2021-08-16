# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    t = len(cc[:-4]) # calculating the lenth for the # string
    temp = t*"#" # creating a temporary hash string
    ans = temp + cc[-4:] # creating the answer string
    return ans

def maskify(cc):
    return "#" * len(cc[:-4]) + cc[-4:]

