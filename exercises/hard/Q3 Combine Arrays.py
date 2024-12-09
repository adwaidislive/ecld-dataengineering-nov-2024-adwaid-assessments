"""
Create a function that takes three lists and returns one list where all passed arrays are combined into nested lists.


These lists should be combined based on indexes: the first nested list should contain only the items on index 0, the second list on index 1, and so on.


If any list contains fewer items than necessary, supplement the missing item with "*".
"""

def combine_lists(lst1,lst2,lst3):
    if len(lst1) >len(lst2):
        if len(lst1) > len(lst3):
            n = len(lst1)
        else:
            n = len(lst3)
    else:
        if len(lst2) > len(lst3):
            n = len(lst2)
        else:
            n = len(lst3)
            
    lst4 = []
    for i in range(n):
        lst4.append([])
        
        try:
            lst4[i].append(lst1[i])
        except IndexError:
            lst4[i].append("*")
        
        try:
            lst4[i].append(lst2[i])
        except IndexError:
            lst4[i].append("*")
        
        try :
            lst4[i].append(lst3[i])
        except IndexError:
            lst4[i].append("*")
        
    return lst4