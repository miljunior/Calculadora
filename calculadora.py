def entrada():
	print ("\nEscolha a operação: ")
	return int(input ("\n1 - Soma \n2 - Subtração \n3 - Divisão \n4 - Multiplicação \n0 - Sair \n\nDigite aqui o número da operação: "))

def saida():
    print ("\nEscolha a opção: ")
    return int(input ("\n0 - Sair \n5 - Novo Calculo \n\nDigite aqui o número da opção: "))

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

operacao = ["Sair", "Soma", "Subtração", "Divisão", "Multiplicação"]

print ("::: Calculadora MJ:::")
op = entrada()

while (op >= 1 and op <=4):

	print ("Opção escolhida: ", operacao[op],"\n")

	num1 = int(input("Insira o primeiro valor: "))
	print()
	num2 = int(input("Insira o segundo valor: "))
	print()

	if op == 1:	
		print("Resultado: ", soma(num1, num2), "\n\n")

	elif op == 2:
		print("Resultado: ", subtracao(num1, num2), "\n\n")

	elif op == 3:
		print("Resultado: ", divisao(num1, num2), "\n\n")

	elif op == 4:
		print("Resultado: ", multiplicacao(num1, num2), "\n\n")

	op = saida()

	while op == 5:
		op = entrada()

else:
	print("Obrigado por usar a calculadora")
