#Implement a function that checks if a number is even.
#Return "Even" or "Odd" accordingly.

def is_even(x):
    if (x % 2):
        return ("Odd")
    else:
        return ("Even")
    
#Write a function reverse_string(s) that returns the reverse of a string.
#Example:
#Input: "hello"
#Output: "olleh"

def reverse_string(s):
    return s[::-1]

#Complete a função para retornar apenas os números pares de uma lista, mantendo a ordem:

def filter_even(numbers):
    result = []
    for n in numbers:
        if not (n % 2):
            result.append(n)
    return result