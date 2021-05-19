# what are dictionaries
# are structured as KEY = VALUE
# VALUE could be a string, int, list
# syntax = {}

student_1 = {
    'name': 'James',
    'key': 'value',
    'stream': 'Cyber Security',  # string
    'completed_lessons': 3,  # int
    'completed_lesson_names': ["variables", "operators", "data_collections"]  # list

}

print(student_1)  # prints out the whole dictionary
print(student_1['completed_lesson_names'])  # prints the value from the given key
print(student_1['completed_lesson_names'][2])  # prints one index from the list
print(student_1.keys())  # only prints the keys within the dictionary
print(student_1.values())  # only prints the values within the dictionary
