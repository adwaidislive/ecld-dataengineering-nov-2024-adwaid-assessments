# Grocery Store Prices
"""
You are given a list of strings consisting of grocery items, with prices in parentheses. Return a list of prices in float format.

Examples
get_prices(["salad ($4.99)"]) ➞ [4.99]

get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
])

➞ [1.99, 5.99, 0.75]

get_prices([
  "ice cream ($5.99)",
  "banana ($0.20)",
  "sandwich ($8.50)",
  "soup ($1.99)"
])

➞ [5.99, 0.2, 8.50, 1.99]
"""

def get_prices(lst):
    
    lst1 = [((price.split('$')[1])) for price in lst]
    lst2 = []
    for i in range(len(lst1)):
        val = lst1[i].replace(')','')
        lst2.append(float(val))

    return (lst2)

print(get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
]))