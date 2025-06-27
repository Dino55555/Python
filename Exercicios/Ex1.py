#Implement a function negate_array(arr) that returns a new array with all numbers negated.
#Example: [1, -2, 3] → [-1, 2, -3]

def negate_array(arr):
    result = []
    for x in arr:
        result.append(-x)
    return result

#Write a Python function count_negatives(arr) that returns how many negative numbers are in the array.
#Example:
#Input: [1, -3, 0, -5]
#Output: 2

def count_negatives(arr):
    cont = 0
    for i in arr:
        if i < 0:
            cont = cont + 1
    return cont