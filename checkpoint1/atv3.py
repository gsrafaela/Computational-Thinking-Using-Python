consumo_media_ano_anterior = float(input("Informe a média de consumo de água, em m³, no ano anterior: "))
consumo_mes_vigente = float(input("Informe o consumo de água, em m³, do mês vigente: "))


if consumo_mes_vigente <= 20:
    valor_consumo = consumo_mes_vigente*2
elif consumo_mes_vigente >20 and consumo_mes_vigente <=35:
    valor_consumo = consumo_mes_vigente*3.5
elif consumo_mes_vigente >35 and consumo_mes_vigente <=50:
    valor_consumo = consumo_mes_vigente*5.5
elif consumo_mes_vigente >50:
    valor_consumo = consumo_mes_vigente*7

if consumo_mes_vigente < consumo_media_ano_anterior:
    desconto = valor_consumo*0.2
    total_conta = valor_consumo - desconto
    print("O valor total da conta é de:", total_conta, "E o valor do desconto é de:", desconto)
elif consumo_mes_vigente > consumo_media_ano_anterior*1.1:
    multa = valor_consumo*0.3
    total_conta = valor_consumo + multa
    print("O valor total da conta é de:", total_conta, "E o valor do multa é de:", multa)
else:
    print("O valor total da conta é de:", valor_consumo, "e não houve multa ou desconto.")


