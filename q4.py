# 4. (25 points) Write a Python function `printStats(t)` which retrives data in a text file _t_ which reads in lines of numbers.  
# For each line read in, the function must call a _decorator_ function which prints 

# * the numbers read
# * the count of the numbers read
# * the average of the numbers
# * the maximum of the numbers


# decorator function to count & print list of numbers
def decorator(func):
    def wrapper(numbers):
        result = func(numbers)
        count = len(result)
        average = sum(result) / count
        maximum = max(result)

        print("Numbers read:", result)
        print("Count of numbers read:", count)
        print("Average of numbers:", average)
        print("Maximum of numbers:", maximum)

        return result

    return wrapper

def read_numbers(line):
    #takes string "line" as input, strips any leading or trailing whitespace, splits string into list of strings, converting to "int" type value, returns list of integers
    return list(map(int, line.strip().split()))

def printStats(t):
    # read and open file 
    with open(t, 'r') as file:
        for line in file:
            read_numbers(line)

# test
read_numbers = decorator(read_numbers)
printStats('q4.txt')
