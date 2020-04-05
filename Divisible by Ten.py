"""
Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
Return the count of how many numbers in the list are divisible by 10.
"""

# Method 1
"""
a = []


def divisible_by_ten(nums):
    for element in nums:
        if element % 10 == 0:
            a.append(element)

    return len(a)


print(divisible_by_ten([20, 25, 30, 35, 40]))
"""

# Method 2

def divisible_by_ten(nums):
    a = 0
    for element in nums:
        if element % 10 == 0:
            a = a + 1

    return a


print(divisible_by_ten([20, 25, 30, 35, 40]))
