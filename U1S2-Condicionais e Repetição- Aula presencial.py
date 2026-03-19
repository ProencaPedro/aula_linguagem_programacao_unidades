"""
                EXERCÍCIOS

1. Escreva um código que verifica se um número é par ou
ímpar.
2. Crie um programa que peça ao usuário sua idade e diga
se ele pode votar (no Brasil: voto a partir de 16 anos).
3. Faça um laço for que exiba os números de 1 a 10.
4. Escreva um programa que conte até 10 usando while.
5. Crie um programa que peça um número e exiba a
tabuada dele.
6. Faça um loop que pare quando o usuário digitar 0.
7. Crie um código que conte quantos números pares
existem entre 1 e 50.
8. Escreva um for que exiba os múltiplos de 3, até 30.
9. Faça um código que só aceite números positivos. Se o
usuário digitar um número negativo, peça novamente.
10. Escreva um loop que inverta uma string digitada pelo
usuário (por exemplo: ele digita ONIBUS e o programa
escreve SUBINO).
"""
# 1:
n = int(input("Insira um numero: "))

if n % 2 == 0:
  print("Esse numero é par")
else:
  print("Esse numero é impar")

# 2:
i = int(input("Insira sua idade: "))

if i > 16:
  print("Parabéns! Você está apto a votar!")
else: 
  print("Que pena. Você não está apto a votar.")

#3:
for i in range(1, 11):
  print(i)

#4:
contador = 0
while contador < 11:
  print(contador)
  contador += 1

#5: 
numero = int(input("Insira um número, para ver sua tabuada: "))
print(f"Tabuada do {numero}:")
for i in range(1,11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

#6:
print("--Descubra a Tabuada de qualquer numero! (Digite 0 para sair)--")

print("\n")

while True:
  numero = int(input("Insira um número, para ver sua tabuada:"))

  if numero == 0:
    print("Programa encerrado... Até logo!")
    break

  print(f"Tabuada do {numero}:")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#7:
contador_pares= 0
for n in range(1, 51):
  if n % 2 == 0:
    contador_pares = contador_pares + 1

print(f"Existem {contador_pares} números pares entre 1 a 50.")

#8:
contador_multiplo_3 = 0
for n in range(1, 31):
  if n % 3 == 0:
    contador_multiplo_3 = contador_multiplo_3 + 1

print(f"Existem {contador_multiplo_3} número multiplos por 3 de 1 a 30. ")

#9:
while True:
  n = float(input("Digite apenas números postivios: "))
  if n >= 0:
    print(f"Número {n} aceito com sucesso!")
    break

  print("Error....Você digitou um número negativo. Tente novamnete.")

print("Fim do programa.")

#10:
t = input("Digite uma palavra ou frase: ")
t_invert = ""

for letra in t:
  t_invert = letra + t_invert

print(f"O inverso de {t} é: {t_invert}")








