# Basic Arithmetic Operations on a String Number
"""
Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
"""

def arithmetic_operation(n):
    n = n.split(' ')
    if(n[1] == '+'):
        return (int(n[0]) + int(n[2]))
    elif(n[1] == '-'):
        return (int(n[0]) - int(n[2]))
    elif(n[1] == '*'):
        return (int(n[0]) * int(n[2]))
    elif(n[1] == '//'):
        if(int(n[2]) == 0):
            return -1
        else:
            return (int(n[0]) // int(n[2]))
        
print(arithmetic_operation("12 + 12"))