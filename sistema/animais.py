class Animal:
    contador = 0

    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.id = Animal.contador + 1
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade
        Animal.contador = self.id
