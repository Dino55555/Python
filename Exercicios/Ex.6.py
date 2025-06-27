#Implemente a função sort_by_frequency(nums: list[int]) -> list[int] 
#que retorna a lista ordenada por frequência (menos frequentes vêm primeiro). 
# Se dois números tiverem a mesma frequência, o maior número vem primeiro.

#Exemplo:

#sort_by_frequency([4,4,1,1,1,2,2,3])  # [3,2,2,4,4,1,1,1]

def sort_by_frequency(nums):
    # 1. Contar a frequência de cada número
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # 2. Ordenar os números com base em:
    #    (frequência crescente, valor decrescente)
    nums_sorted = sorted(nums, key=lambda x: (freq[x], -x))

    return nums_sorted



    

