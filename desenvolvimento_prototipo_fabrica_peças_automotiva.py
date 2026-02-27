#Cliente relata que tem aumentado o número de peças e que gostaria de uma solução que fosse capaz de prever quantas peças erão vendias em um determinado mês.
#Esse resuultado é importante para ele, uma vez que dependendo da quantidade, ele preicsa contratar mais funcionários, reforçar seu estoque e prever horas extras.
#LINK DO PROTOTIPO NO COLAB: https://colab.research.google.com/drive/1mh7lR9l5MLSpiV-29vUbSGUd2TZcXxDy#scrollTo=4n3AEwEkhDUL

#Prototipo:
c = 200 #valor da constante
mes = input("Digite o mês que deseja saber o resultado: ")
mes = int(mes) #Converter para numérico o valor captura pela função input()

r = c * mes
print(f"A quantidade de peças para o mês {mes} será {r}")
