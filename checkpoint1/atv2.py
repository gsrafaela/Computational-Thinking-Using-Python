consumo_mensal = int(input("Informe a quantidade de kWh consumida no mês: "))

while consumo_mensal < 0:
    print("Resposta inválida, consumo menor que 0")
    consumo_mensal = int(input("Informe a quantidade de kWh consumida no mês: "))
if consumo_mensal <= 50:
    valor_kwh = 14
elif consumo_mensal >=51:
    valor_kwh =  14 + (consumo_mensal*0.25)

if consumo_mensal <= 99:
    aliquota = 0
elif consumo_mensal >=100 and consumo_mensal <= 200:
    aliquota = 0.13
elif consumo_mensal >=201:
    aliquota = 0.33

calculo_icms = valor_kwh*aliquota
total_conta = valor_kwh + calculo_icms

print("O valor do seu consumo mensal foi:", valor_kwh, "e o valor do ICMS foi:", calculo_icms, "portanto, o total da conta é de:", total_conta, "reais.")

