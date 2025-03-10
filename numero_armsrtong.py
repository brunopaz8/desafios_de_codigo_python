#Um número Armstrong (também chamado de número de Narciso) é um número que é igual à soma de seus próprios dígitos elevados à potência do número de dígitos.

def numero_armstrong(numero):
    tamanho = len(str(numero))
    resultado = 0
    for digito in str(numero):
        resultado += int(digito) ** tamanho
    return numero == resultado


numero = int(input('Selecione um numero: '))

if numero_armstrong(numero=numero) == True:
    print('É um numero Armstrong!')
else:
    print('Não é um numero Armstrong!')