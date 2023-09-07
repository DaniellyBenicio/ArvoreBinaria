'''Implemente um método na classe `Arvore` que permite a remoção de um nó específico da árvore.'''

#se no interno e tem filho na esquerda e direita um dos dois filhos deve substituir o pai, quem deve substituir é o maior numero, 
# pega sempre o da esquerda para a raiz e o da direita para a esquerda


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

    def procurar(self, v):
        if self.raiz is None: 
            return False
        else:
            return self._procurar(self.raiz, v) 
    
    def _procurar(self, no, v):
        if no is None: 
            return False
        if no.valor == v: 
            return True
        if self._procurar(no.esquerda, v):
            return True
        if self._procurar(no.direita, v): 
            return True

    def nos_internos(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self._nos_internos(self.raiz)

    def _nos_internos(self, no):
        if no is not None:
            if no.esquerda is not None and no.direita is not None:
                print(no.valor, end=' ')
            self._nos_internos(no.esquerda)
            self._nos_internos(no.direita)

    def folhas(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self._folhas(self.raiz)

    def _folhas(self, no):
        if no is not None:
            if no.esquerda is None and no.direita is None:
                print(no.valor, end=' ')
            self._folhas(no.esquerda)
            self._folhas(no.direita)
            
    def remover(self, v):
        if self.raiz is None:
            return None
        else:
            return self._remover(self.raiz, v)
    
    def _remover(self, no, v):
        if no is None:
            return None
        if v < no.valor:
            no.esquerda = self._remover(no.esquerda, v)
        elif v > no.valor:
            no.direita = self._remover(no.direita, v)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
        
            #remover elemento quando ele possui dois filhos.

            menor_valor_D = self._menor_valor(no.direita)

            no.valor = menor_valor_D
            no.direita = self._remover(no.direita, menor_valor_D)
        return no

    def _menor_valor(self, no):
        if no.esquerda is None:
            return no.valor
        else:
            return self._menor_valor(no.esquerda)
        

'''     5

    3      7

2   4    6   8'''
qnt = int(input('Digite quantos nós deseja inserir na árvore: '))
def inserir(arv):
    for i in range(qnt):
        n = int(input(f'Informe o {i+1}º número: '))
        arv.inserir_em_nivel(n)
    print('Números inseridos na árvore: ')
    arv.mostrar_pre_ordem()

def verificar_e_remover(arv):
    v = int(input('Informe o número para verificar presença e remover da árvore: '))
    if arv.procurar(v):
        print(f'O número {v} está presente na árvore!')
        arv.remover(v)
        print(f'O nó {v} foi removido com sucesso!')
        print()
        print('A árvore agora possui esses nós: ')
        arv.mostrar_pre_ordem()
    else:
        print('Número não está presente na árvore!')

arvore = ArvoreBinaria()
inserir(arvore)
print()
verificar_e_remover(arvore)
