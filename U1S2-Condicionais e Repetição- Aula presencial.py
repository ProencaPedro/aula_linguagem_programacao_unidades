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
  
