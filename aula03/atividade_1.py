valor_antes = 83
percentual = float(input('Qual o percentual do desconto? '))/100
desconto = 83 * percentual
valor_depois = 83 - desconto

print('Você vai ganhar', f'{desconto:.2f}', 'reais de desconto')
print('O preço final será', valor_depois, 'reais')