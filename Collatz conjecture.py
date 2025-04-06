def steps(number):
    '''
    Take any positive integer n. If n is even, divide n by 2 to get n / 2. 
    If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. 
    
    The conjecture states that no matter which number you start with, you will always 
    reach 1 eventually.

    :param number: int - number to check the collatz conjecture
    '''
    cc = 1
    step =0

    if number<=0:
        raise ValueError("Only positive integers are allowed")

    while number != cc:
        step = step + 1
        if number % 2 == 0:
            number = number/2
        else:
            number = (3*number)+1
    
    return step

steps(45)