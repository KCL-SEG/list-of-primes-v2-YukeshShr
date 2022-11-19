"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    if(number_of_primes <= 0):
        raise ValueError("Invalid Number! Argument must be greater than 0")
    else:
        while(len(list) < number_of_primes):

            for i in range(2, count):
                if(count % i == 0):
                    break
            else:
                list.append(count)
            
            count += 1
        return list