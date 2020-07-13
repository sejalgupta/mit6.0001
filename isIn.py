#Bisection algorithm to depict what isIn does
#aStr must be in alphabetical order

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) < 1: 
        return False
    if len(aStr) == 1:
        if aStr == char:
            return True
        return False
    num = int(len(aStr)/2)
    if (aStr[num] == char):
        return True
    elif (aStr[num] < char):
        return isIn(char, aStr[num+1:])
    else:
        return isIn(char, aStr[:num - 1])
