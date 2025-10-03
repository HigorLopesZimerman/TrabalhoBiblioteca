class No:
    
    def __init__(self, chave, posicao):
        self.chave = chave
        self.posicao = posicao
        self.left = None
        self.right = None


class Arvore:
    
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, posicao):
        if self.raiz is None:
            self.raiz = No(chave, posicao)
        else:
            self._inserir(self.raiz, chave, posicao)

    def _inserir(self, no, chave, posicao):
        if chave < no.chave:
            if no.left is None:
                no.left = No(chave, posicao)
            else:
                self._inserir(no.left, chave, posicao)
        elif chave > no.chave:
            if no.right is None:
                no.right = No(chave, posicao)
            else:
                self._inserir(no.right, chave, posicao)

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if no is None:
            return None
        if chave == no.chave:
            return no.posicao
        elif chave < no.chave:
            return self._buscar(no.left, chave)
        else:
            return self._buscar(no.right, chave)

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is not None:
            self._em_ordem(no.left, resultado)
            resultado.append((no.chave, no.posicao))
            self._em_ordem(no.right, resultado)

    def construir_arvore(self, registros, campo_chave="codigo"):
        for pos, reg in enumerate(registros):
            self.inserir(reg[campo_chave], pos)
