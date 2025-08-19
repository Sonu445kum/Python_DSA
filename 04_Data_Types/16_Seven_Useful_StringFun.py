# 1=> Capitalize() 
# Capitalize is Used in the python for Converting the First Character into Uppercase 
# And The Rest of ZThe Character remain will same

# input from users
sentence_1 = "mY name is YUVRAJ"
sentence_2 = "MY name is Ansul"

# Convert case using capitalize()
capitalized_string = sentence_1.capitalize()
print("Sentence 1 output -> ", capitalized_string)
capitalized_string = sentence_2.capitalize()
print("Sentence 2 output -> ", capitalized_string)

# 2 => Count()
# The count() is used in Python to count the number of occurrences of an individual
#  element or substring that appears within the string. The count() throws the numeric
#  value that provides the detail of an actual count of a given string.

message = 'GFG KARLO HO JAYEGA'

# number of occurrence of 'G'
print('Number of occurrence of G:', message.count('G'))


# 3 => Find()
# The find() is used in Python to return the lowest index value from the first occurrence of 
# a string (only in case if its found): else the value would be -1.
message = 'Yuvraj is my name'

# check the index of 'is'
print(message.find('is'))


# 4 => Lower()
# The lower() is used in Python programming to ensure that all the UPPERCASE
#  characters in the string are converted into lowercase and fetched with a
#  new lowercase string and the original copy of the string remains intact.
message = 'GEEKSFORGEEKS IS A COMPUTER SCIENCE PORTAL'

# convert message to lowercase
print(message.lower())

# 5 => Upper()
# The upper() is used in Python programming to ensure that all the lowercase
#  characters in the string are converted into UPPERCASE and fetched with a 
# new string whereas the original copy of the string remains intact.
message = 'geeksforgeeks is a computer science portal'

# convert message to uppercase
print(message.upper())

# 6 =>Replace()
# The replace() is used in Python to replace any unwanted character or text 
# and replace it with the new desired output within the string. 
# The replace() can be used in Python with the below-mentioned syntax to perform the action:


# Syntax
# string.replace(old, new, count)
text = 'subway surfer'

# replace s with t
replaced_text = text.replace('s', 't')
print(replaced_text)