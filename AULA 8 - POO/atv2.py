class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

# Exemplo de uso:
pessoa1 = Pessoa(
    nome="Maria", idade=30, peso=65, genero="Feminino"
)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Gênero: {pessoa1.genero}")
