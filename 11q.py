'''Escreva uma função que verifica se uma árvore binária é uma árvore de busca válida.'''

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

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def mostrar_em_nivel(self):
        if self.raiz is None:
            return
        else:
            print(self.raiz.valor, end= ' ')
            self.mostrar_em_nivel_recursivo(self.raiz)
        
    def mostrar_em_nivel_recursivo(self, no):
        if no.esquerda is not None:
            print(no.esquerda.valor, end= ' ')
        if no.direita is not None:
            print(no.direita.valor, end=' ')
        
        if no.esquerda is not None:
            self.mostrar_em_nivel_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_em_nivel_recursivo(no.direita)
                
    def busca_arv_valida(self):
        if self.raiz is not None:
            if self.raiz.esquerda is None and self.raiz.direita is None:
                return True
            else: 
                menor_valor = float('-inf') # menor valor possivel
                maior_valor = float('inf') # maior valor possivel
                return self._busca_arv_valida(self.raiz, menor_valor, maior_valor)
                
        return False # arvore é vazia
    
    def _busca_arv_valida(self, no, menor_valor, maior_valor):
        if no is None:
            return True
        if menor_valor < no.valor < maior_valor:
            return (self._busca_arv_valida(no.esquerda, menor_valor, no.valor) 
                    and self._busca_arv_valida(no.direita, no.valor, maior_valor))
        else:
            return False
          

def inserir():
    arvore = ArvoreBinaria()
    
    qnt = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt):
        num = int(input(f'Digite o {i+1}º valor: '))
        arvore.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')
    arvore.mostrar_em_nivel()
    print()
    
    return arvore

arvore = inserir()
    
if arvore.busca_arv_valida():
    print("A árvore é uma árvore de busca válida.")
else:
    print("A árvore não é uma árvore de busca válida.")
