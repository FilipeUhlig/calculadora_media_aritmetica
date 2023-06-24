"""
Programa: Calculadora de média aritmética de quatro fatores.
Descrição: Este programa calcula a média aritmética de quatro valores.
Autor: Filipe
Data: 06/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis

#Entrada de dados
n1 = float(input("Qual é o primeiro valor? "))
n2 = float(input("Qual é o segundo valor? "))
n3 = float(input("Qual é o terceiro valor? "))
n4 = float(input("Qual é o quarto valor? "))

#Processamento de dados
media = ((n1+n2+n3+n4)/4)

#Saida de dados
print(f"A média aritmética de {n1, n2, n3, n4} é {media}.")