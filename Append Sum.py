"""
Write a function named append_sum that has one parameter — a list named named lst.
The function should add the last two elements of lst together and append the result to
lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
"""


def append_sum(lst):
    # lst = [1, 1, 2]
    sum_1 = lst[-2] + lst[-1]
    lst = lst + [sum_1]

    sum_2 = lst[-2] + lst[-1]
    lst = lst + [sum_2]

    sum_3 = lst[-2] + lst[-1]
    new_list = lst + [sum_3]
    return new_list


print(append_sum([1, 1, 2]))
