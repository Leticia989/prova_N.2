def pedir_numero():
    while True:
        try:
            numero = int( input( 'Informe um numero' ))
            return numero
            break
        except ValueError:
            print( 'numero invalido' )
    return pedir_numero()

def tratar_numero():
    numeros = pedir_numero()
    soma = 0
    maior = 0
    menor = 0
    for i in range(numeros):
        n = float( input( 'digite um numero' ) )
        maior+=1
        menor+=1
        soma+=n
        if maior != 0 and maior > n :
            print(maior)
        elif menor != 0 and menor < n :
            print(menor)
    print(f' O menor numero é: {menor}, O mairo número é: {maior}' )
    media = soma / numeros
    print( 'A média dos numeros digitadas foi de:', media )
    return tratar_numero


pedir_numero()
tratar_numero()


