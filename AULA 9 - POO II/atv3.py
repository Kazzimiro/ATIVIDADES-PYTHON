class Calculadora:
    def somar(self, a, b):
        return a + b

# Exemplos de uso
calc = Calculadora()

# Somando números inteiros
resultado_inteiros = calc.somar(5, 3)
print(f"Soma de números inteiros: {resultado_inteiros}")

# Somando strings
resultado_strings = calc.somar("Olá ", "Mundo")
print(f"Soma de strings: {resultado_strings}")
