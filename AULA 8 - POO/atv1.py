class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def exibir_informacoes(self):
        return f'Nome: {self.nome}, Raça: {self.raca}, Idade: {self.idade} anos'

# Exemplo de uso
meu_cachorro = Cachorro("Rex", "Labrador", 5)
print(meu_cachorro.exibir_informacoes())
