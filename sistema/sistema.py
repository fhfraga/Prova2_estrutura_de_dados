from sistema.animais import Animal
from sistema.pessoas import Pessoa


class Sistema:
    contador = 0

    def __init__(self):
        self.id = Sistema.contador + 1
        self.animais = []
        self.pessoas = []
        Sistema.contador = self.id

    def cadastrar_animal(self, tipo, idade, cor, porte, particularidade):
        animal = Animal(tipo, idade, cor, porte, particularidade)
        self.animais.append(animal)

    def cadastrar_pessoa(self, nome, telefone, email, especie, preferencia):
        pessoa = Pessoa(nome, telefone, email, especie, preferencia)
        self.pessoas.append(pessoa)

    def todos_animais(self):
        dicionario = {}
        for animal in self.animais:
            print(f'id: {animal.id}')
            print(f'tipo: {animal.tipo}')
            print(f'idade: {animal.idade}')
            print(f'cor: {animal.cor}')
            print(f'porte: {animal.porte}')
            print('----------------------------')

    def gerar_relatorio(self):
        for pessoa in self.pessoas:
            print(f'Relatório Nº {self.id}')
            print(f'Candidato: {pessoa.nome}')
            print(f'Espécie de interesse: {pessoa.especie}')
            print('Animais correspondentes:')
            for animal in self.animais:
                if animal.tipo == pessoa.especie:
                    print(
                        f'-Id animal {animal.id} ,Tipo: {animal.tipo}, Idade: {animal.idade}, Cor: {animal.cor}, Porte: {animal.porte}, Particularidade: {animal.particularidade}')
                    idade = 0
                    cor = 0
                    porte = 0
                    if animal.porte == pessoa.preferencia:
                        porte = 1 * 0.8
                    if animal.idade == pessoa.preferencia:
                        idade = 1 * 0.6
                    if animal.cor == pessoa.preferencia:
                        cor = 1 * 0.4
                    pessoa.pontuacao = porte + idade + cor
                    print(
                        f'A pontuação do usuário para o animal de id {animal.id} é: {pessoa.pontuacao}')
            print('---------------------------------------')

    def pesquisar_animal(self, tipo, idade, cor, porte, particularidade):
        for animal in self.animais:
            if animal.tipo == tipo and animal.idade == idade and animal.cor == cor and animal.porte == porte and animal.particularidade == particularidade:
                print(f'O animal pesquisado é o animal de Id {animal.id}')
        return 'Nenhum animal encontrado com tais características'
