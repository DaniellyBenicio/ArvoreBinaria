'''Escreva uma função que retorna todos os nós em um determinado nível da árvore.'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)            
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)  
    
    def altura(self):
        if self.raiz is None:
            return 0
        else:
            return self._altura(self.raiz) 
    
    def _altura(self, no):
        if no is None:
            return 0
        altura_e = 0
        altura_d = 0

        if no.esquerda is not None:
            altura_e = 1 + self._altura(no.esquerda)
        if no.direita is not None:
            altura_d = 1 + self._altura(no.direita)
        if altura_e > altura_d:
            return altura_e
        else:
            return altura_d
                
    def nos_no_nivel(self, nivel):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            altura = self.altura()
            if nivel > altura:
                print()
                print('Esse nível não existe na árvore.')
            else:
                self._nos_no_nivel(self.raiz, nivel, 0)
    
    def _nos_no_nivel(self, no, nivel, nivel_atual):
        if nivel == 0:
            print(self.raiz.valor)
        elif no is not None:
            if nivel == nivel_atual:
                print(no.valor, end=' ')
            else:
                self._nos_no_nivel(no.esquerda, nivel, nivel_atual + 1)
                self._nos_no_nivel(no.direita, nivel, nivel_atual + 1)
                
def nos_por_nivel():
    arvore = ArvoreBinaria()
    
    qnt = int(input('Quantos valores deseja inserir na árvore: '))
    for i in range(qnt):
        n = int(input(f'Digite o {i+1}º valor: '))
        arvore.inserir_em_nivel(n)
    print('Valores inseridos com sucesso na árvore!')
    
    print()
    nivel = int(input('Informe o nível para mostrar os nós: '))
    print(f'Os nós no nível {nivel} são:' ,end=' ')
    arvore.nos_no_nivel(nivel)
    print()

nos_por_nivel()