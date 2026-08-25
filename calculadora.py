import math

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

class calculadora:
    def __init__(self):
        self.resultado = 0

    def somar(self, a, b):
        self.resultado = a + b
        return self.resultado
    def subtrair(self, a, b):
        self.resultado = a - b
        return self.resultado
    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado
    def divisao(self, a, b):
        try:
            self.resultado = a / b
            return self.resultado
        
        except ZeroDivisionError:
            return "Erro: Divisao por zero não é permitido."

calc = calculadora()


print(calc.somar(a,b))
print(calc.subtrair(a,b))
print(calc.multiplicar(a,b))
print(calc.divisao(a,b))





