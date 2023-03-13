tabuada = int (input("Digite um numero para exibir a tabuada: "))
print("A tabuada do numero", tabuada, " é: ")
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))