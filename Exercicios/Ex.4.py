#Complete a função get_max_word que deve receber uma frase e retornar a palavra de maior comprimento.

def get_max_word(sentence):
    words = sentence.split()
    max_word = ""
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word