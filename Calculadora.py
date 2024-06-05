
class Operacoes:
    def __init__(self, valorA, operador, valorB):
        self.valorA = valorA
        self.operador = operador
        self.valorB = valorB
        self.resultado = None

class Calculadora:
    def calcular(self, operacao):
        if operacao.operador == '+':
            operacao.resultado = self.soma(operacao)
        elif operacao.operador == '-':
            operacao.resultado = self.subtracao(operacao)
        elif operacao.operador == '*':
            operacao.resultado = self.multiplicacao(operacao)
        elif operacao.operador == '/':
            operacao.resultado = self.divisao(operacao)
        else:
            operacao.resultado = 0


    def soma(self, operacao):
        return operacao.valorA + operacao.valorB

    def subtracao(self, operacao):
        return operacao.valorA - operacao.valorB

    def multiplicacao(self, operacao):
        return operacao.valorA * operacao.valorB
    
    def divisao(self, operacao):
        return operacao.valorA / operacao.valorB
    

