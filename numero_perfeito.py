#Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios

def numero_perfeito(numero):
    contador = numero -1
    
    soma_divisores = 0
    
    while contador > 0:
        if numero % contador == 0:
            soma_divisores += contador
            contador -= 1
        else:
            contador -= 1
    
    return soma_divisores == numero

numero = int(input('Selecione um numero: '))

if numero_perfeito(numero=numero) == True:
    print('É um numero perfeito!')
else:
    print('Não é um numero perfeito!')