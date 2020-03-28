"""
Create a function named same_name() that has two parameters named your_name and my_name.
If our names are identical, return True. Otherwise, return False.
"""


def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False
