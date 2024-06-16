class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: R${funcionario.salario:.2f}")

# Exemplo de uso:
if __name__ == "__main__":
    empresa = Empresa()

    joao = Funcionario("João", "Desenvolvedor", 5000)
    maria = Funcionario("Maria", "Gerente", 8000)

    empresa.adicionar_funcionario(joao)
    empresa.adicionar_funcionario(maria)

    empresa.listar_funcionarios()
