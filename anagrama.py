#Dois textos são considerados anagramas se podemos reorganizar as letras de um para formar o outro.

def anagrama(palavra1, palavra2):

    return sorted(palavra1.lower().replace(' ','')) == sorted(palavra2.lower().replace(' ','')) 

palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunda palavra: ')
resposta = anagrama(palavra1=palavra1, palavra2=palavra2)

if resposta == True:
    print('São anagramas!')
else:
    print('Não são anagramas!')