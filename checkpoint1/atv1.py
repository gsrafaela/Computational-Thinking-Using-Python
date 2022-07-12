anos = int(input("Informe a quantidade de anos: "))
meses = int(input("Informe a quantidade de meses: "))
t = int(input("Informe t: "))

total_meses = anos*12 + t + meses
novo_ano = total_meses // 12
novo_mes = total_meses % 12

print("O novo tempo após o inteiro t é:", novo_ano, "ano(s) e", novo_mes, "meses.")