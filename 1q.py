'''Crie uma classe `No` que represente um nó em uma árvore binária. A classe deve ter atributos para armazenar o valor do nó, o nó esquerdo e o nó direito.'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None