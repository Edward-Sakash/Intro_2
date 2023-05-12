# Dictionarries

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict['name']
my_dict['age']
my_dict['city']

my_list = ['Alice', 25, 'New York']
my_list[0]

bob_dict = {'name': 'Bob', 'boss': [{'name': 'Jeremy'}, {'name': 'John'}]}
print(bob_dict['boss'][0]['name'])

for employee in bob_dict['boss']:
    print(employee['name'])

students_entity = {'name': 'bob', 'name': 'john', 'age': 21, 'courses': ['Math', 'Biology']}
print(students_entity)

my_list = ['Bob', 'Bob', 'John']
my_dict = {}
my_dict[my_list[0]] = '_'
my_dict[my_list[1]] = '_'
my_dict[my_list[2]] = '_'
print(my_dict)
my_dict = {}
my_dict['bob'] = 'First value'
my_dict['bob'] = 'Second value'
my_dict['john'] = 'Third value'
print(my_dict)

### fromkeys():
#The fromkeys() method creates a new dictionary with the specified keys and values.

my_keys = ['name', 'age', 'city']
my_dict = dict.fromkeys(my_keys, '_')
print(my_dict)

my_dict = {}
for key in my_keys:
    my_dict[key] = '_'
print(my_dict)    

### get():

### setdefault(): method returns the value for specified key.


my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'Germany'}
my_dict.setdefault('name', 'Bob')
my_dict.setdefault('country', 'USA')
print(my_dict)
my_dict['country'] = 'Germany'
print(my_dict['country'])

### update

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
new_dict = {'country': 'USA', 'age': 26}
my_dict.update(new_dict)
print(my_dict)

my_dict['zip'] = 3333
print(my_dict)

my_dict.items()
print(my_dict.items())

for item in my_dict.items():
    key = item[0]
    value = item[1]
                 
    print(key, value)

nested_list = [(1,2), (3,4)]   
a,b = nested_list
print(a,b)     

print(my_dict.keys())

for value in my_dict.values():
    print(value)
    