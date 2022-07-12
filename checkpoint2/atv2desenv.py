n = int(input("Informe a quantidade de produtos: "))
i = 1
maior_real = ""
maior_percent = ""

preco_atual = float(input("Informe o preço atual do {}° produto: ".format(i)))
preco_reajustado = float(input("Informe o preço reajustado do {}° produto: ".format(i)))

#calculo variação real
variacao_real = preco_reajustado-preco_atual
maior_real = variacao_real

#calculo desconto percentual
if preco_atual > preco_reajustado:
   percentual = (preco_atual-preco_reajustado)/preco_atual*100
   maior_percent = percentual
   #print("O reajuste foi de -{}%".format(percentual))

#calculo aumento percentual
elif preco_atual < preco_reajustado:
    percentual = (preco_reajustado-preco_atual)/preco_atual*100
    maior_percent = percentual
    #print("O reajuste foi de {}%".format(percentual))

while i < n:
    i = i+1
    preco_atual = float(input("Informe o preço atual do {}° produto: ".format(i)))
    preco_reajustado = float(input("Informe o preço reajustado do {}° produto: ".format(i)))

    variacao_real = preco_reajustado-preco_atual
    if variacao_real > maior_real:
        maior_real = variacao_real

    if preco_atual > preco_reajustado:
        percentual = (preco_atual-preco_reajustado)/preco_atual*100
        if percentual > maior_percent:
            maior_percent = percentual
   #print("O reajuste foi de -{}%".format(percentual))

#calculo aumento percentual
    elif preco_atual < preco_reajustado:
        percentual = (preco_reajustado-preco_atual)/preco_atual*100
        if percentual > maior_percent:
            maior_percent = percentual
    #print("O reajuste foi de {}%".format(percentual))

if maior_real <=0:
    print("Não houve aumento em nenhum produto")
else:
    print("O maior aumento real entre os {} produtos foi de {}, e a maior aumento percentual foi de {}%".format(n, maior_real, maior_percent))


