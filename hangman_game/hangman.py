def put_underline(word):
    aux = ""
    for x in word:
        aux = aux + "_ "
    return aux

def verify_guess(word, secret, guess):
    aux = ""
    i = 0

    while i < len(word): 
        if word[i] == guess:
            aux = aux + guess + " "
        else:
            aux = aux + secret[2 * i] + " "
        i = i + 1
    return aux


word = input("Inform the hangman word: ").upper()
errors = 0

secret = put_underline(word)


while errors < 6 and "_" in secret:
    print(secret)
    print("Errors: {}".format(errors))
    guess = input("Letter: ").upper()
    secret2 = verify_guess(word, secret, guess)

    if secret == secret2:
        errors = errors + 1
    else:
        secret = secret2

if errors >= 6:
    print("YOU LOSE!! THE WORD WAS: {}".format(word))
else:
    print("YOU WIN!! THE WORD WAS: {}".format(word))