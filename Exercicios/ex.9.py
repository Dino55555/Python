#Escreva a função:

# def find_pair_with_sum(arr, target):
#Que retorna uma tupla com os dois primeiros números que somam exatamente target.
#Se não encontrar, retorna None.

#Exemplo:

#find_pair_with_sum([3, 5, 2, -4, 8, 11], 7)
# → (5, 2)

def find_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None
