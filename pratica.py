nome = 'Pablo'
idade = 25;

n1 = input(f'Olá, tudo bem {nome}?\nSua idade é {25}!') 
print('Você esta estudando com a', 'A','L','U','R','A', sep='\n')



# Exercício: Escolher entre ímpar ou par

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O numero e par.')
else:
    print('O numero e impar.')

# Exercício: Classificar faixa etária com base na idade

idade = int(input('Digite sua idade: '))

if idade < 12:
    print("Você é criança")
elif idade < 18:
    print("Você é adolescente")
else:
    print("Você é adulto")


