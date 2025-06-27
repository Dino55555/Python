#Implemente a função longest_prefix(words: list[str]) -> str
#que deve retornar o prefixo comum mais longo de todas as palavras de uma lista.

#Exemplos:

#longest_prefix(["flower", "flow", "flight"])  # "fl"
#longest_prefix(["dog", "racecar", "car"])     # ""
#Regras:

#A função deve ter complexidade no máximo O(n·m), sendo:

#n = número de palavras
#m = comprimento médio de cada palavra

#Seja legível e evite comparações desnecessárias

def longest_prefix(words):
    if not words:
        return ""
    
    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


