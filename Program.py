from Pilha import Pilha

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


def calculadora():
    operacoes = []
    pilha_resultados = Pilha()
    continua = ""
    while continua != 'N':
        operacao = input("Escolha uma operação (+, -, *, /): ")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = adicao(num1, num2)
            print("O resultado da adição é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}")
            print("Lista de operações:", operacoes)  # Imprime após o cálculo
            pilha_resultados.empilhar(resultado)
        elif operacao == "-":
            resultado = subtracao(num1, num2)
            print("O resultado da subtração é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}")
            print("Lista de operações:", operacoes)  # Imprime após o cálculo
            pilha_resultados.empilhar(resultado)
        elif operacao == "*":
            resultado = multiplicacao(num1, num2)
            print("O resultado da multiplicação é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}")
            print("Lista de operações:", operacoes)  # Imprime após o cálculo
            pilha_resultados.empilhar(resultado)
        elif operacao == "/":
            resultado = divisao(num1, num2)
            print("O resultado da divisão é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}")
            print("Lista de operações:", operacoes)  # Imprime após o cálculo
            pilha_resultados.empilhar(resultado)
        else:
            print("Operação inválida!")
        continua = (input("Deseja continuar 'S' para sim, 'N' para Não."))

    print("Pilha de resultados finais:", pilha_resultados.itens)    
    print("Calculadora encerrada!")
    
calculadora()