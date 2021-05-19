# Lists the syntax is []

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