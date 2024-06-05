from Operacoes import Operacoes
from Pilha import Pilha


def calculadora():
    operacoes = []
    pilha_resultados = Pilha()
    continua = ""
    while continua != 'N':
        operacao = input("Escolha uma operação (+, -, *, /): ")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        

        if operacao == "+":
            resultado = Operacoes.adicao(num1, num2)  #faz as operacoes necessarias pro resultado
            print("O resultado da adição é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}") #mostra o que foi usado e guarda em uma lista
            print("Lista de operações:", operacoes)
            pilha_resultados.empilhar(resultado) #vai armazenando o resultado em uma pilha para mostrar ao final
        elif operacao == "-":
            resultado = Operacoes.subtracao(num1, num2)
            print("O resultado da subtração é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}")
            print("Lista de operações:", operacoes)
            pilha_resultados.empilhar(resultado)
        elif operacao == "*":
            resultado = Operacoes.multiplicacao(num1, num2)
            print("O resultado da multiplicação é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}")
            print("Lista de operações:", operacoes)
            pilha_resultados.empilhar(resultado)
        elif operacao == "/":
            resultado = Operacoes.divisao(num1, num2)
            print("O resultado da divisão é:", resultado)
            operacoes.append(f" {num1} {operacao}  {num2}")
            print("Lista de operações:", operacoes)
            pilha_resultados.empilhar(resultado)
        else:
            print("Operação inválida!")
        continua = (input("Deseja continuar 'S' para sim, 'N' para Não.").upper())

    print("Pilha de resultados finais:", pilha_resultados.itens)    
    print("Calculadora encerrada!")
    
calculadora()