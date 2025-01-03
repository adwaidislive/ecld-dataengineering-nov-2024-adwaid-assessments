# Layers in a Rug

"""
Write a function that counts how many concentric layers a rug has.

Examples
count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]) ➞ 2

count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
]) ➞ 3

count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
]) ➞ 5
Notes
Multiple layers can share the same component so count them separately (example #2).
Layers will be horizontally and vertically symmetric.
There will be at least one layer for each rug.
"""

def count_layers(rug):
    lst1 =[]
    for i in rug:
        if i not in lst1:
            lst1.append(i)
    return len(lst1)


print(count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]))