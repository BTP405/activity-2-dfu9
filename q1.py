## helper function to determine if prime number
def isPrime(num):
    ## 1st prime number is 2 so if n less than 2 return false
    if num < 2:
        return False

    ## checks if numbers (i) in range is divisible
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

## Function to get prime numbers
def getPrimeNumbers(n):
    ## create list
    primes = []
    ##loop to test if numbers(i) in range are prime numbers
    for i in range(2, n + 1):
        ## if true, add to list 
        if isPrime(i):
            ##append adds item to end of the list
            primes.append(i)
    return primes

## testing
n = 100
prime_numbers = getPrimeNumbers(n)
print(f"{prime_numbers}")
