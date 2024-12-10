"""
Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
"""

def remove_letters(letters, word):
    for l in word:
        if l in letters:
            letters.remove(l)
    return letters