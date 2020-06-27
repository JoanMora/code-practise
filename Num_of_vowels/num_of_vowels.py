'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(input_str):
    vowels = ['a','e','i','o','u']
    num_vowels = len(list(filter(lambda letter: letter in vowels, input_str)))
    return num_vowels
