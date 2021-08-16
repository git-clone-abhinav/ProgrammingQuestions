def digital_root(n):
    if len(str(n))==1: # checking for len==1 int
           return n
    else:
            sum = 0 # temporary variable sum
            for i in str(n): # iteration
                sum = sum + int(i) # sumvalue increment
            if len(str(sum)) > 1: # checking if lenght of string of sum is still > 1
                return (digital_root(sum)) # if yes -> recurssion
            else:
                return sum # if no -> returning the value

def digital_root(n):
    return n%9 or n and 9 

def digital_root(n):
    return 1 + ((int(n) - 1) % 9) if n>0 else 0

import functools
def digital_root(n):
    while (n > 9):
        n = functools.reduce(lambda a, b: int(a) + int(b), list(str(n)))
    return n