
# Write a Python program that sorts a list of tuples based on the second element of each tuple.
# The program should take a list of tuples as input from the user,
# sort the tuples by the second element using the sort() method with a custom function
# print the sorted list of tuples

print("________________________________________")
# Solution 1
# define a list of tuples
"""tuple_list = [(2, 5), (1, 7), (4, 3), (6, 1), (3, 8)]

# define a function that takes a tuple and returns its second element
def sort_by_second(tuple_item):
    return tuple_item[1]

# use the sorted function with the key parameter to sort the tuples by their second element
sorted_tuples = sorted(tuple_list, key=sort_by_second)

# print the sorted list of tuples
print(sorted_tuples)
"""
print("________________________________________")

"""# Solution 2
# Take input from user as list of tuples
tuple_list = eval(input("Enter a list of tuples: "))

# Define a custom function to use as key in the sort method
def sort_by_second(elem):
    # Returns the second element of a tuple for sorting
    return elem[1]

# Sort the list of tuples based on the second element using the custom function
tuple_list.sort(key=sort_by_second)

# Print the sorted list of tuples
print(tuple_list)"""

print("________________________________________")

# Bonus solution 

# take input from user as a list of tuples
tuple_list = [(2, 5), (1, 7), (4, 3), (6, 1), (3, 8)]

# define a helper function to extract the second element of each tuple
# we use a lambda function here which is an anonymous function that takes one argument (tuple_item)
# and returns the second element of the tuple (tuple_item[1])
sort_by_second = lambda tuple_item: tuple_item[1]

# sort the list of tuples based on the second element of each tuple using the sort() method and the helper function
sorted_tuples = sorted(tuple_list, key=sort_by_second)

# print the sorted list of tuples
print(sorted_tuples)


