from sistema.sistema import Sistema

# Exemplo de uso
sistema = Sistema()

# Cadastro de animais
sistema.cadastrar_animal("canino", "adulto", "marrom", "médio", "nenhuma")
sistema.cadastrar_animal("felino", "jovem", "preto", "pequeno", "nenhuma")

# Cadastro de pessoas
sistema.cadastrar_pessoa("Marcio", "123456789",
                         "marcio@gmail.com", "canino", "nenhuma")
sistema.cadastrar_pessoa("Fernando", "789456123",
                         "fernando@gmail.com", "canino", "marrom")
sistema.cadastrar_pessoa("Alessandra", "987654321",
                         "alessandra@gmail.com", "felino", "nenhuma")

# Ver todos os animais
print('Relatório de todos os animais')
sistema.relatorio_todos_animais()
print('----------------------\n')

# Geração de relatório
print('Geração de relatório')
sistema.gerar_relatorio()
print('----------------------\n')

# Pesquisa por animal
print('Pesquisa de animal com todas as caracteristicas')
animal_encontrado = sistema.pesquisar_animal(
    "canino", "adulto", "marrom", "médio", "nenhuma")
animal_encontrado
print('----------------------\n')

print('Pesquisa de animal pelo porte')
print('Pesquisa binária recursiva')
sistema.pesquisar_animal_pesquisa_binaria_recursiva('médio')
