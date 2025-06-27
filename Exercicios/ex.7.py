#Implemente a função:

# def compress_string(s: str) -> str:
#Que recebe uma string e retorna uma versão comprimida onde caracteres consecutivos iguais são substituídos por apenas um seguido da contagem.

#Exemplo:

#compress_string("aaabbc")    # "a3b2c1"
#compress_string("abc")       # "a1b1c1"
#compress_string("aabcccccaaa") # "a2b1c5a3"
#Regras:

#Se o resultado for maior ou igual à string original, retorne a original

#Ex: "abcd" → "a1b1c1d1" → retorne "abcd"

def compress_string(s):
    if not s:
        return s

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1

    result.append(s[-1] + str(count))  # último grupo

    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s
