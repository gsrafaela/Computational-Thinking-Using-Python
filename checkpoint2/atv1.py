n = int(input("Informe n: "))
acum = 1
i = 1

while n <=0:
    print("Não ha sequência, pois N é menor ou igual que 0")
    n = int(input("Informe n: "))
    
num_seq = int(input("Informe o {}° da sequencia: ".format(i)))
num_bckp = num_seq

while i < n:
    i = i+1
    num_seq = int(input("Informe o {}° numero da sequencia: ".format(i)))
    if num_seq != num_bckp:
        acum = acum + 1
    num_bckp = num_seq

print(acum)