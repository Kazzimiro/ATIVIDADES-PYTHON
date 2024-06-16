class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None
    
    def definir_cor(self, cor):
        self.cor = cor
        return self
    
    def definir_modelo(self, modelo):
        self.modelo = modelo
        return self

class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = "Carro"

class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = "Bicicleta"

# Exemplo de uso
carro = Carro().definir_cor("Azul").definir_modelo("Sedan")
print(f"Tipo: {carro.tipo}, Cor: {carro.cor}, Modelo: {carro.modelo}")

bicicleta = Bicicleta().definir_cor("Vermelha").definir_modelo("Mountain Bike")
print(f"Tipo: {bicicleta.tipo}, Cor: {bicicleta.cor}, Modelo: {bicicleta.modelo}")
