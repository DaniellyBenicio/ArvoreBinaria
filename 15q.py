'''Escreva uma função que, dado um nó, retorne todos os nós filhos do nó fornecido.'''

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
                
    def filhos_do_no(self, valor):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            buscar_no = self.buscar_no(self.raiz, valor)
            if buscar_no is not None:
                if buscar_no.esquerda:
                    print(buscar_no.esquerda.valor, end=' ')
                if buscar_no.direita:   
                    print(buscar_no.direita.valor, end=' ')
                print()
                if not buscar_no.esquerda and not buscar_no.direita:
                    print(f'O nó {valor} não possui filhos.')
            else:
                print(f'O nó {valor} não está presente na árvore.')

    def buscar_no(self, no, valor):
        if no is None:
            return None
        if no.valor == valor:
            return no
        esquerda = self.buscar_no(no.esquerda, valor)
        if esquerda:
            return esquerda
        direita = self.buscar_no(no.direita, valor)
        return direita
     
def busca_no_arvore():
    arvore = ArvoreBinaria()
    
    qnt = int(input('Quantos valores deseja inserir na árvore?: '))
    for i in range(qnt):
        n = int(input(f'Digite o {i+1}º valor: '))
        arvore.inserir_em_nivel(n)
    print('Valores inseridos com sucesso na árvore!')
    
    print()
    no = int(input('Digite um nó para mostrar seus filhos: '))
    arvore.filhos_do_no(no)
    print()
    
busca_no_arvore()
