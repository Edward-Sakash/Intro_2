# Collection

my_list = [1,2,3,4,5]
"""my_list = []
my_list = list()"""

my_list[2] = 6
print(my_list)

my_list2 = my_list
my_list

(id(my_list), id(my_list2))
my_list2[0] = 'Hello World'
print(my_list2)

my_tuple = (1,2,3,4,5)
my_tuple

my_tuple2 = my_tuple

my_tuple = ('hello', 1, True, [1,2])
my_tuple[0]
print(my_tuple[0])

my_tuple[3][0] = 'Changed!'
print(my_tuple[3][0])

my_list = [1,2, ('hello', 'again')]
my_list
print(my_list)

for index in range(len(my_list)):
    print(my_list[index])


my_list = [1,2,3, 'four', 5]
print(my_list.index('four'))
print(my_list.count(5))

my_list[:3] + [5] + my_list[3:]

my_list.insert(3, 'New VALUE')
print(my_list)

my_new_list= my_list[::-1]


my_list = [3,2,1,5,4]
print(sorted(my_list))
print(my_list)

my_list = [1,2,3,'four', 5.0]
#my_list.extend([6,7,8])
print(my_list)

my_new = my_list[::] + [6,7,8]
print(my_new)

#my_list = [3,2,1,5,4]
#print (my_list.sort())
my_list = [3,2,1,5,4]
print (sorted(my_list))
print(my_list)

strings = ['Hello', 'world', 'again', 'bla']

length = []

for word in strings:
    length.append(len(word))
length

length = [len(word) for word in strings]
uppercase_words = [word.upper() for word in strings]
print(uppercase_words)

list_numbers = [[5,6,3], [8,3,1], [9,10,4], [8,4,9]]
list_numbers[0][0]

my_sums = [sum(nums) for nums in list_numbers]# [14,12,23,14]
my_sums = [nums[0] + nums[1] + nums[2] for nums in list_numbers]
my_sums = [max(nums) for nums in list_numbers] #[6,8,10,8]

def capitalize_long_strings(lst):
    result = []
    for item in lst:
        if len(item) >= 5:
            #result.append(item.capitalize())
            result.append(item.upper())
    return result




lst = ["apple", "banana", "cat", "dog", "elephant", "frog"]
print(capitalize_long_strings(lst))