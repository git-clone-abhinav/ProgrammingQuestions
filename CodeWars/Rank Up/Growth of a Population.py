# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

def nb_year(p0, percent, aug, p):
    count = 0 # counter
    while(p > p0): # using while loop instead of recursion to avoid recursive increment of the counter
        p0 = int(p0 + (percent / 100) * p0 + aug) # formula
        count += 1 # counter increment
        
    return count