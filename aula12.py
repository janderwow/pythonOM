# exercicios IMC
nome = 'Jander WoW'
altura = 1.79
peso = 84
imc = peso / (altura ** 2) # peso / (altura X altura)

#exibir o seguinte texto
# Jander WoW tem 1.79 de altura
# peso 84 quilos e seu imc é
# 1123123.12312312312

print('Jander Wow tem', altura,'de altura')
print('Pesa', peso,'quilos e seu IMC e')
print(imc)

# utilizando fstring
print(f'Jander WoW tem {altura} de altura')
print(f'Pesa {peso} quilos e tem IMC e {imc}')