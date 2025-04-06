def is_armstrong_number(number):
    '''
    This function will answer if the given number is an armstron number, meaning it is a number 
    that is the sum of its own digits each raised to the power of the number of digits.

    :param number: int - number to check it is an armstron number
    :return: "{number} is an armstron number or {number} is not an armstron number"

    '''
    arm_num = 0
    for n in enumerate(str(153)):
        num = int(n[1])**(len(str(153)))
        arm_num = arm_num + num
        print(arm_num)

    return number==int(arm_num)

is_armstrong_number(153)