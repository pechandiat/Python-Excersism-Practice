def square(number):
    if 1 <= number <= 64:
        grains = 2**(number-1)
    else:
        raise ValueError("Square number must be between 1 and 64")
    
    return grains

def total():
    grains=0
    for n in range(1,65):
        grains = grains+(2**(n-1))
    
    return round(grains,0)


#square(5)
total()