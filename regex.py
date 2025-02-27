"""""
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
print(x)
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) 
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object 
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) 
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
"""
"""""



#in this file i will work with python RegEx exercises
#task1
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
"""""
import re
def match_pattern(input_string):
    pattern=r"ab*"
    if re.fullmatch(pattern, input_string):
        return True
    else:
        return False

test_strings = ["a", "ab", "abb", "abbb", "b", "ba", "abc","ДУБЛИКАТ","aab"]
for test in test_strings:
    result = match_pattern(test)
    print(f"'{test}': {result}")
    

#task2
#Write a Python program that matches a string that has an 'a' followed by two to three 'b'


import re
def match1(input_string):
    pattern=r"ab{2,3}"
    if re.fullmatch(pattern, input_string):
        return True
    else:
        return False
tests=["abb", "ab"]
for test in tests:
    result = match1(test)
    print(f"'{test}': {result}")


#task3
#Write a Python program to find sequences of low
# ercase letters joined with a underscore.
import re

def find_sequences(input_string):
    matches = re.findall(pattern, input_string)
    return matches

test_string = input("Тестийн утгаа оруулна уу: ")  # Тестийн утга оруулах хэсэг
result = find_sequences(test_string)
print(f"Олдсон дарааллууд: {result}")


#task4
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

def find_sequences(input_string):
    pattern = r"[A-Z][a-z]+"
    matches = re.findall(pattern, input_string)
    return matches

test_string = "This is a TestString with SomeUppercase Words"
result = find_sequences(test_string)
print(f"Sequences: {result}")


#task5
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

def match_pattern(input_string):
    pattern = r"a.*b$"
    if re.fullmatch(pattern, input_string):
        return True
    else:
        return False

test_strings = ["ab", "acb", "a12345b", "abc", "a", "ba"]
for test in test_strings:
    result = match_pattern(test)
    print(f"'{test}': {result}")


#task6
#Write a Python program to replace all occurrences of space, comma, or dot with a colon

import re

def replace_with_colon(input_string):
    pattern = r"[ ,.]"
    result = re.sub(pattern, ":", input_string)
    return result

test_string = "Hello, world. This is a test, with spaces."
result = replace_with_colon(test_string)
print(f"Modified string: {result}")
# task7
#Write a python program to convert snake case string to camel case string
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_case_str = components[0] + ''.join(word.title() for word in components[1:])
    return camel_case_str

snake_str = "this_is_a_snake_case_string"
camel_case_str = snake_to_camel(snake_str)
print("Camel Case:", camel_case_str)
#output :
#Camel Case: thisIsASnakeCaseString

#task 8
#Write a Python program to split a string at uppercase letters
import re

def split_at_uppercase(s):
    return re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', s)


input_str = "ThisIsAStringWithUppercaseLetters"
result = split_at_uppercase(input_str)
print(result)
# output:
# ['This', 'Is', 'A', 'String', 'With', 'Uppercase', 'Letters']

#task 9
# Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

input_str = "ThisIsAStringWithCapitalLetters"
result = insert_spaces(input_str)
print(result)
#output:
# This Is A String With Capital Letters

# task 10
# Write a Python program to convert a given camel case string to snake case
import re

def camel_to_snake(camel_str):
   
    snake_case_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_case_str

camel_str = "thisIsCamelCaseString"
snake_case_str = camel_to_snake(camel_str)
print(snake_case_str)
#output :
# this_is_camel_case_string