class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero"

# Exemplo de uso
calc = Calculadora()

print("Soma:", calc.somar(10, 5))
print("Subtração:", calc.subtrair(10, 5))
print("Multiplicação:", calc.multiplicar(10, 5))
print("Divisão:", calc.dividir(10, 5))
print("Tentativa de divisão por zero:", calc.dividir(10, 0))
