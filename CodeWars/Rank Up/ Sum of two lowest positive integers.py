# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    numbers.sort(key=int) # sorting
    return numbers[0]+numbers[1] # sum of first and second element
    #return numbers[0]+numbers[1]