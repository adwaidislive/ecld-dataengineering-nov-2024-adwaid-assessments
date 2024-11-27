"""
Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your function.

The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".

"""

def is_prime(primes,num):
    high = len(primes)-1
    low = 0
    def binarySearch(primes,low,high,num):
        if high>=low:
            mid = low + (high - low) // 2
            if primes[mid] == num:
                return 'yes'
            
            elif (num < primes[mid]):
                return binarySearch(primes, low, mid-1, num)
        
            else:
                return binarySearch(primes, mid+1, high, num)
            
        else:
            return 'no'
        
    return binarySearch(primes,low,high,num)
        
        
