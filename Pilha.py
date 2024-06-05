class Pilha:
    def __init__(self):
        self.itens = []
    def empilhar (self, item):
        self.itens.append(item)
    def desempilhar(self):
        if self.vazia():
            return None
        else:
            return self.itens.pop()
    def vazia (self):
        return len(self.itens) == 0