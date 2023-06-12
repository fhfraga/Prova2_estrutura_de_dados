class Pessoa:
    contador = 0
    pontuacao = 0

    def __init__(self, nome, telefone, email, especie, preferencia):
        self.id = Pessoa.contador + 1
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.especie = especie
        self.preferencia = preferencia
        Pessoa.contador = self.id
        self.pontuacao = Pessoa.pontuacao
