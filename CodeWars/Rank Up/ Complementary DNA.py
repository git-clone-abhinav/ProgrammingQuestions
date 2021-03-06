# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    compliment = {"A":"T","T":"A","G":"C","C":"G"} # a dictionary mapping to the compliments
    temp = "" # a temporary string
    for elem in dna: # character iterator
        temp = temp + compliment[elem]
    return temp

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])