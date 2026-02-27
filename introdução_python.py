print("Hello world!")
Hello world!
print(2 + 3 * 5)
17

#Variáveis são espaços alocados na memória RAM para guardar valores temporariamente.
#A variavel especifica o tipo de dado que ela guardará.
#Python é capaz de determinar o tipo de dado da variável com base no seu valor,ou seja, as variáveis são tipadas dinaminamente nessa linguagem.
x = 10 
nome = 'aluno'
nota = 8.75
fez_inscricao = True
#Para saber o tipo de dado que uma variável guarda, podendo imprimir seu tipo usando a função type().
print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))

#Para solicitar que o usuário digite um nome, a função input() faz a leitura de um valor digitado.


nome = input("Digite um nome: ")
print(nome)

#Existem variedade de formas de imprimir texto e varável em Pythom. Podemos usar formatadores de caracteres (igual em C), podemos usar a função format() e podemos criar uma sting formatada.

#Modo 1 - usando formatadores de caracteres (igual na linguagem C) para imprimir variável e texto
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro Hello world" % (nome))

#Modo 2 - usando a função format() para imprimir variável e texto.
print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro Hello world".format(nome))

#Modo 3 - usando string formatadas
print(f"Olá {nome}, bem vindo a disciplina de pogramação. Parabéns peo seu primeiro Hello world")

#Operações matemáticas suportadas por Python:
x + y #Soma de x e y
x - y #Diferença de x e y
x * y #Produto de x e y
x / y #Quociente de x e y
x // y #Parte inteira do quociente de x e y
x % y #Resto de x / y 
abs(x) #Valor absoluto de x 
pow(x,y) #x elevado a y
x ** y # x elevado a y

#Qual o resultado armazenado na variável da operacao_1 e operacao_2
operacao_1 = 2 + 3 * 5
print(f"Resultado em operacao_1 = {operacao_1}")
 Resultado em operacao_1 = 17
operacao_2 = (2 + 3) * 5
print(f"Resultado em operacao_2 = {operacao_2}")
 Resultado em operacao_2 = 25

#Tentar fazer uma equação de segundo grau y=a * x ** 2 + b * x + c, onde a,b, c são constantes.
# O valor de y(resultado) depende do valor de x, ou seja, x é a variável independente e y a dependente.
#Vamos solicitar para o usuário um valor de x e retornar o valor de y correspondete ao x que ele digitou.
a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

y = a * x ** 2 + b * x + c
print(f"O resultado de y para x = {x} é {y}.")
 Traceback (most recent call last):
   File "/home/main.py", line 6, in <module>
    y = a * x ** 2 + b * x + c
            ~~^^~~
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#Esse erro significa que estamos tentando fazer uma operação matemática entre string e um tipo numérico. Então alguma variáveis deve ter um tipo errado.
#Usando a função type() verificamos os tipos das variáveis usadas.
print(type(a))
print(type(b))
print(type(c))
print(type(x))
<class 'int'>
<class 'float'>
<class 'int'>
<class 'str'>
#O tipo de variável x é string(str), isso acontece porque ao usar a função  iput(), ela retorna uma string, independente do que o usuario digitou, sempre seá string.
#Precisamos converter o resultado da entrada em um tipo numérico.
#Como não sabemos se o usuário vai digitar um número inteiro ou decimal, vamos fazer a conversão usando a funcção float().
a = 2 
b = 0.5
c = 1 
x = input("Digite o valor de x: ")

x = float(x) # Aqui é feita a conversão da string para o tipo numérico

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")
Digite o valor de x: 3
O resultado de y para x = 3.0 é 20.5.



#ESTRUTURAS LÓGICAS, CONDICIONAIS E DE REPETIÇÃO EM PYTHON

#Em Python tudo é objeto, então uma variável também é um objeto.

#Operados relacionais
a < b #O valor de a é menor que b?
a <= b #O valor de a é igual OU menos que b?
a > b #O valor de a é maior que b?
a >= b #O valor de a é maior OU igual que b?
a == b #O valor de a é igual ao de b?
a != b #O valor de a é diferente do valor de b? 
a is b #O valor de a é idêntico ao valor de b?
a is not b #O valor de a não é idêntico ao valor de b?

#Estruturas Condicionais em Python: IF, ELIF, ELSE
#O comando if..else.. significam se..senão.. e são usados para contruir as estruturas condicionais.

#Python possui uma sintaxe especial para a construção das estruturas condicionais.

#Estrutura  condicional simples
a = 5
b = 10

if a < b :
 print("a é menor do que b")
 r = a + b 
 print(r)

#Estrutura condicional composta:
a = 10
b = 5

if a < b:
 print("a é menor do que b")
 r = a + b
 print(r)
else:
 print("a é maior do que b")
 r = a - b
 print(r)

#Para construir uma estrutura encadeada, devemos usar o comando "elif", que é uma abreviação de else if. 
codigo_compra = 5111

if codigo_compra == 5222:
 print("Compra à vista.")

elif codigo_compra == 5333:
 print("Compra à prazo no boleto.")

elif codigo_compra == 5444:
 print("Código não cadastrado")

else:
 print("Código não cadastrado")

#Estrutura Lógicas em python : AND, OR , NOT
















