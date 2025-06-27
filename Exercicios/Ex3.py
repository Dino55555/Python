#Complete the class to reserve medium tables only:

#class MediumOnlyReservation:
#    def __init__(self, medium):
#        self.medium = medium
#
#    def reserve(self):
#        if self.medium > 0:
#            ________
#            return True
#        return False

class MediumOnlyReservation:
    def __init__(self, medium):
        self.medium = medium

    def reserve(self):
        if self.medium > 0:
            self.medium = self.medium - 1
            return True
        return False
    
#Implement a class Counter with two methods:
#__init__ that starts the count at 0
#increment() that increases the count by 1
#get() that returns the current count

class Counter:
    def __init__(self):
        self.x = 0
    def increment(self):
        self.x = self.x + 1
    def get(self):
        return self.x        
    
#You are given the following incomplete function:

# def find_max(arr):
#    max_value = arr[0]
#    for num in arr:
        # Fill this part
#    return max_value
#Complete the function so that it returns the largest number in the list.

def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if max_value < num:
            max_value = num 
    return max_value

#Encontre e corrija os erros neste código:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name} and I'm {self.age} years old.")

#Implemente em Python uma classe BoundedStack que funciona como pilha mas tem capacidade máxima (max_size). Deve oferecer:
#push(item): adiciona se não estiver cheia, retorna True ou False.
#pop(): remove e retorna o topo, ou None se vazia.
#is_full() e is_empty().

class BoundedStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Stack = []
    
    def is_full(self):
        if len(self.Stack) < self.max_size:
            return 1

    def is_empty(self):
        if len(self.Stack) == 0:
            return 1
    
    def push(self, item):
        if self.is_full:
            return False
        else: 
            self.Stack.append(item)
            if len(self.Stack) == self.max_size:
                self.is_full = True    
            return True

    def pop(self):
        if self.is_empty:
            return None
        else:
            self.Stack.pop(0)
            return self.Stack[0]

    