cedula = int(input("Insira o valor da célula que você deseja trocar: "))
moeda_a = int(input("Insira o valor de uma moeda que você deseja trocar: "))
moeda_b= int(input("Insira o valor da outra moeda que você deseja trocar: "))

checagem = False
i= 0 
j = 0 

if cedula%moeda_a == 0:
    resultado = cedula/moeda_a
    print("{} moedas de {}".format(resultado, moeda_a))
elif cedula%moeda_b == 0:
    resultado = cedula/moeda_b
    print("{} moedas de {}".format(resultado, moeda_b))

else:
    for i in range (cedula):
        for j in range (cedula):
            total = moeda_a*i+moeda_b*j
            if total == cedula:
                checagem = True
                break
        if total == cedula:
            checagem = True
            break

    if checagem == True:    
        print("{} moedas de {} e {} moedas de {}".format(i, moeda_a, j, moeda_b))
    else:
        print("Não é possível fazer a troca")