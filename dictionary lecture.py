my_dict = {(1,2): 'Hello'}
print(hash('Hello'))

dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (86, 'India'),
    (62, 'Indonezia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]
#country_dial = {key:value for code in dial_codes}
country_dial = {code[1]: code[0] for code in dial_codes}
print(country_dial)

one_item = ('Germany', 49)
country, dial_num = one_item
#print(country, dial_num)
print(country_dial)

my_country_code = {code: country.upper() for country, code in country_dial.items() if code<70}
print(my_country_code)

list(zip(range(3), 'ABC'))
print(list(zip(range(3), 'ABC')))

list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))
print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))

from itertools import zip_longest

print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))

list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1))
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))

#print(list(zip([1,2], 'ABC', strict=True)))


list(enumerate('ABC', start =1))
print(list(enumerate('ABC', start =1)))

my_fruits = ['apple', 'banana', 'melon']

for integer, value in enumerate(my_fruits, start=1):
    #print(integer, value)
    print(f"{integer}. {value}")

a = [(1,2,3),
     (4,5,6)]
list(zip(a[0], a[1]))
print(list(zip(a[0], a[1])))

print("______________________________________")


zen_python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
"""words = zen_python.split()
dict_index = {}"""


dict_index = {}
words = zen_python.split()
for index, word in enumerate(words):
    ocurrences = dict_index.get(word, [])
    ocurrences.append(index)
    dict_index[word] = ocurrences

for word in list(dict_index.items())[:3]:
    print(word)    

empty_dict = {'better': 'Hello'}
empty_dict.get('better', [])
print(empty_dict.get('better', []))

words = zen_python.split()
dict_index = {}
for word in words:
    dict_index[word] = []

for index, word in enumerate(words):
    dict_index[word].append(index)
print(dict_index)

words = zen_python.split()
dict_index = {}
for word in words:
    dict_index[word] = []

for index, word in enumerate(words):
    dict_index[word].append(index)
print(dict_index)

nested_list = [[1,2], [3,4]]
for item1, item2 in nested_list:
    print(item1, item2)

import collections

def default_helper():
    return []
my_dict = collections.defaultdict(default_helper)

for index, word in enumerate(words):
    ocurrences = dict_index[word]
    ocurrences.append(index)


for word in list(dict_index.items())[:3]  :
    print(word)

my_dict['key1'] = 'value1'
print(my_dict)
print(my_dict['word'])
print(my_dict['key'])

def default_helper():
    return []

dict_index = collections.defaultdict(default_helper)

for index, word in enumerate(words):
    ocurrences = dict_index[word]
    ocurrences.append(index)

for word in list(dict_index.items())[:3]:
    print(word)

ct = collections.Counter('abracadabra')
print(ct)

ct.update('aaaazzz')
print(ct)

ct.most_common(2)
print(ct.most_common(2))

subjects = [
    {'name': 'English', 'grade': 'A'},
    {'name': 'German', 'grade': 'F'},
    {'name': 'Maths', 'grade': 'F'},
]

ct2 = collections.Counter()

for subject in subjects:
    ct2.update(subject['grade'])

print(ct2['F']) 

grades = [subject['grade'] for subject in subjects]
print(grades)

ct2 = collections.Counter(grades)
print(ct2)

ct2 = collections.Counter(subject['grade'] for subject in subjects)
print(ct2)

l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(set(l))

"""my_hashable_tuple = (1,2)
hash(my_hashable_tuple)
my_unhashable_tuple = (1,2, [])
print(hash(my_unhashable_tuple))"""

"""print(hash(set()))"""

frozenset([1,2,3])

s = set()
type(s)
print(type(s))

s = {1.0, 2.0, 3.0}
s.add(5)
print(s)

s = {1.0, 2.0, 3.0}
s.pop()
"""s.pop()
s.pop()
s.pop()"""
s
print(s)


s = set([1,2,3,4]) # or {1,2,3,4}
print(s)

s_frozen = frozenset([1,2,3,4])
s_frozen 
my_list = list(s_frozen)
print(my_list)

list('Hello')
print(list('Hello'))

l = ['spam', 'spam', 'egg']
print(l.count('spam'))

my_set = {item for item in l}
print(my_set)


A = {1,3,5,7}
B = {1,2,4,6,7}
union = A | B
print(union)

A.union(B)
print(A.union(B))

A.union([40,50])
print(A.union([40,50]))

A = {1,2,5,7}
B = {1,2,4,6}
A & B
print(A & B)

A.intersection(B)
print(A.intersection(B))

C = {1,100}
A.intersection(B, C)
print(A.intersection(B, C))

A = {1,2,3}
B = {}##### not finished!


A = {1,2,3}
B = {3,4}
A^B
print(A^B)

