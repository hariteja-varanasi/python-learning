"""
Strings are sequences of characters, using the syntax of either single quotes or double quotes:
'hello'
"Hello"
"I don't do that"
"""

#indexing
str_var='hello'
print(f"0th char of str_var is {str_var[0]}")
print(f"last character of str_var is {str_var[-1]}")
print(f"second character of str_var is {str_var[1]}")
#reverse indexing
"""
The first character of the string is always positioned at 0 in the case of both normal and reverse indexing
"""
print("Reverse Indexing")
print(f"second character of str_var is {str_var[-len(str_var)+1]}")
print(f"third character of str_var is {str_var[-len(str_var)+2]}")
print(f"fourth character of str_var is {str_var[-len(str_var)+3]}")
print(f"fifth character of str_var is {str_var[-len(str_var)+4]}")

"""
Slicing
"""
print("Slicing")
print(f"first three characters of str_var is {str_var[0:3]}")
print(f"last three characters of str_var is {str_var[-3:]}")
print(f"all characters of str_var except first and last is {str_var[1:-1]}")
print(f"all characters of str_var is {str_var[:]}")