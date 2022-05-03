# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# x = [ [5,2,3], [10,8,9] ] 
# # #[] shows we have alist
# # # [[list1], [list2]]
# # x[1][0] = 15
# print(x[1][0])



# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# students[0]['last_name'] = 'Bryant'
# print(students)
  
# # [] outside mean list, then {} inside list of dictionaries. 
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# z = [ {'x': 10, 'y': 20} ]

# z[0]['y'] = 30
# print(z[0]['y'])
# print(z)


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# challenge 2

# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function
# loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def iterateDictionary(some_list):
#     #for statement is going through and grabbing each dictionary
#     for i in range(0, len(some_list)):
#         person = ''
#         #for loop pulls the keys information from the called dictionary (some_list) at location [i]
#         for k in some_list[i]:
#             person += (f"{k}, - {some_list[i][k]},  ") 
#         print(person)
#             # print(some_list[i][k])

# iterateDictionary(students)


# print(students)

# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# challenge 3

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints 
# the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:


# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def iterateDictionary2(key_name, some_list):
#     x = []
#     for i in range(0, len(some_list)):
#         # x.append(some_list[i][key_name]) ##do not use
#         print(some_list[i][key_name])
#     # return x   ##do not use
# iterateDictionary2('last_name', students)

# print(students[0]['first_name'])

# Iterate Through a Dictionary with List Values # Create a function printInfo(some_dict) that given a dictionary whose .
# values are all lists, prints the name of each key along with the size  # of its list, and then prints the associated values within each key's 
# list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    # print(some_dict)
    # for i in range(0, len(some_dict))
    for key in some_dict:
        count = len(some_dict[key]) 
        print(f"{count} {key.upper()}")
        for value in range (count):
            print(some_dict[key][value])


printInfo(dojo)


# printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
