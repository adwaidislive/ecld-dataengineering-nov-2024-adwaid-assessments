# How Many "Prime Numbers" Are There?
# Create a function that finds how many prime numbers there are, up to the given integer.
"""
prime_numbers(10) ➞ 4
# 2, 3, 5 and 7

prime_numbers(20) ➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19

prime_numbers(30) ➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
"""

def prime_numbers(n):
    if n < 2:
        return 0
    
    primes = [True] * n
    primes[0] = primes[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    
    count = sum(primes)
    return count
