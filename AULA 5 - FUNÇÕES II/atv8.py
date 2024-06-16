def calcular_operacao(num1, num2, operacao):
    operacoes = {
        'adicao': lambda x, y: x + y,
        'subtracao': lambda x, y: x - y,
        'multiplicacao': lambda x, y: x * y,
        'divisao': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero não é permitida."
    }
    return operacoes.get(operacao, lambda x, y: "Erro: Operação não reconhecida")(num1, num2)

# Exemplo de uso da função:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Digite a operação desejada (adicao, subtracao, multiplicacao, divisao): ")

resultado = calcular_operacao(num1, num2, op)
print(f"Resultado da operação {op}: {resultado}")
