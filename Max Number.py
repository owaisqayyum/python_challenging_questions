"""
Create a function called max_num() that has three parameters named num1, num2, and num3.

The function should return the largest of these three numbers. If any of two numbers tie as
the largest, you should return "It's a tie!".
"""


def max_num(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        return num1
    elif (num2 > num1) and (num2 > num3):
        return num2
    elif (num3 > num1) and (num3 > num2):
        return num3
    else:
        return "Its a Tie!"


print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))
print(max_num(2, 2, 3))

