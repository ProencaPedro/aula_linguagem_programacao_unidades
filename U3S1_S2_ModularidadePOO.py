'''
1. Crie uma classe Retangulo com atributos largura e altura, e um método que calcula a área.
'''
class Retangulo:
    
    def __init__(self, largura, altura):
        
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        
        return self.largura * self.altura
        
#INSTANCIAÇÃO
        
novo_retangulo = Retangulo(25, 6)
print(f"A área do retângulo é: {novo_retangulo.calcular_area()}")

'''
2. Crie um módulo operacoes.py com funções soma, subtrai, multiplica e divide.
'''
def soma(a, b):
    return a + b 
    
def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b 
    
def divide(a, b ):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b     

'''
3. Crie uma classe Carro com atributos modelo e ano, e um método descricao que imprime essas informações.
'''

class Carro:
    
    def __init__(self, modelo, ano):
        
        self.modelo = modelo
        self.ano = ano
        
    def dados_carro(self):
        
        print(f"Seu carro tem o modelo: {self.modelo} com o Ano: {self.ano}")
  
novo_carro = Carro('corsa', 2015)
novo_carro.dados_carro()

'''
4. Implemente uma classe Livro que guarda titulo, autor e ano, e um método que verifica se é um livro antigo (antes de 1980).
'''

class Livro:
    
    def __init__(self, titulo, autor, ano):
        
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def livro_antigo(self):
        
        if self.ano < 1980:
            print("Seu livro é antigo!")
        
        else:
            print("Seu livro não é antigo.")
            
novo_livro = Livro('Dom Casmurro', 'Machado de Assis', 1899)
novo_livro.livro_antigo()

'''
5. Crie um módulo chamado texto.py com uma função contar_vogais(texto) que retorna o número de vogais em uma string.
'''
#texto.py
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in texto:
        if letra in vogais:
            contador += 1
            
    return contador
  
#main.py
from texto import contar_vogais

frase = "Contador de Vogais nessa frase"
total = contar_vogais(frase)

print(f"O número de vogais na frase é: {total}")



    
