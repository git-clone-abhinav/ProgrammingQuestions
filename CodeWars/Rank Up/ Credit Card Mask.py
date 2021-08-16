# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    hash_length = len(cc[:-4])
    temp = hash_length*"#"
    ans = temp + cc[-4:]
    return ans