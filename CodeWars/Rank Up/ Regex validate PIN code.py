# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

def validate_pin(pin):
    if len(str(pin)) == 4 or len(str(pin)) == 6: # check length for 4 or 6
        for i in pin: # char iterator
            if i not in "0123456789": # checking if a char not in "0123456789"
                return False # if Yes return False
        return True # if No return True
    else:
        return False # if length is not equal to 4 or 6 return Flase

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()

def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)