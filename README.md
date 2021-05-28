# Python Data Collections
- lists | syntax = [ ] | can be edited/ mutable | type = list
- dictionaries | syntax = {"keys":"values"} | type = dict
- tuples | syntax = ( ) | can't be edited once created/ immutable | type = tuple
- sets | syntax = { } | same as a list, but UNORDERED | type = set

## What are data collections?

The difference between lists and tuples is that tuples cannot be edited once created 
### Lists are mutable
```python
# Lists the syntax is [], it can have multiple data types
shopping_list = ['juice', 'strawberries', 'yogurt', 'chicken', 'raspberries', 'butter']  # a list contains 6 indexes
#                    0           1           2         3             4           5
# print(shopping_list)  # prints the list to the terminal
# print(type(shopping_list))  # prints the data type of the list
# print(shopping_list[3])  # prints the 4th index of list
# print(shopping_list[-1])  # prints the 6th index of list because it is the end of the list
shopping_list[5] = 'oats'
print(shopping_list)  # prints the list to the terminal
shopping_list.append("mango")  # adds pringles to the list
print(shopping_list)  # prints the list to the terminal
shopping_list.remove('oats')  # removes oats from the list
print(shopping_list)  # prints the list to the terminal
shopping_list.pop()  # pop() removes the last item from the list
print(shopping_list)  # prints the list to the terminal
```
###tuples are immutable
```python
# Tuples are immutable
# syntax = ()
essentials = ('eggs', 'milk', 'bread')  # tuple
print(essentials)  # prints the list to the terminal
print(type(essentials))  # prints the data type of the list
# essentials[2] = 'yogurt', doesnt work because it is immutable

student_1 = {
    'name': 'James',
    'key': 'value',
    'stream': 'Cyber Security',  # string
    'completed_lessons': 3,  # int
    'completed_lesson_names': ["variables", "operators", "data_collections"]  # list

}

print(student_1['completed_lessons'])
print(student_1['completed_lesson_names'])
print(student_1['completed_lesson_names'][2])  # prints one index from the list
print(student_1.keys())  # only prints the keys within the dictionary
print(student_1.values())  # only prints the values within the dictionary

```
###sets
```python
# sets are a data collection but they are UNORDERED
# syntax name = {}

car_parts = {'wheels', 'doors', 'engine'}
print(car_parts)
car_parts.add('windows')
print(car_parts)
car_parts.remove('doors')
print(car_parts)

#frozen sets
frozen_set = ([1,3,5,6])
print(frozen_set)
```