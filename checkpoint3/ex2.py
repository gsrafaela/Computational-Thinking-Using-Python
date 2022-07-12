def conta_vogal(palavra):
    i = 0
    for letra in palavra:
        if letra in "aeiouAEIOU": #foi usado aeiouAEIOU para o programa reconhecer letras maiúsculas e minusculas
            i = i + 1
    return i

#Testar função
print(conta_vogal("Teste"))