#Implemente uma classe QueueWithMax, que simula uma fila (FIFO), com os seguintes métodos:

#.enqueue(x) → adiciona ao final  
#.dequeue()  → remove do início  
#.get_max()  → retorna o maior elemento da fila, em O(1)
#Você pode usar estruturas auxiliares, mas o get_max não pode varrer a lista toda.

class QueueWithMax:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.is_empty:
            print('Queue is already empty')
        else:
            self.queue.pop(0)

    def get_max(self):
        return max(self.queue)