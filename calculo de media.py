quantidade_de_calculos = int(input('quantos numeros deverão ser usados para calcular essa media? min 2 e max 5: '))

if quantidade_de_calculos == 2:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    media = (n1 + n2) / 2
    print(f'A média entre {n1} e {n2} é {media}.')
elif quantidade_de_calculos == 3:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    n3 = int(input('Digite o terceiro numero: '))
    media = (n1 + n2 + n3) / 2
    print(f'A média entre {n1},{n2} e {n3} é {media}.')
elif quantidade_de_calculos == 4:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    n3 = int(input('Digite o terceiro numero: '))
    n4 = int(input('Digite o quarto numero: '))
    media = (n1 + n2 + n3 + n4) / 2
    print(f'A média entre {n1},{n2},{n3} e {n4} é {media}.')
elif quantidade_de_calculos == 5:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    n3 = int(input('Digite o terceiro numero: '))
    n4 = int(input('Digite o quarto numero: '))
    n5 = int(input('Digite o quinto numero: '))
    media = (n1 + n2 + n3 + n4 + n5) / 2
    print(f'A média entre {n1},{n2},{n3},{n4} e {n5} é {media}.')
else:
    print('voce precisa digitar um numero de 2 a 5.')



