# Classe Livro.
class Livro:
    def __init__(self, titulo, autor, ISBN, ano_publicacao, disponibilidade=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = ISBN
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade

    def __str__(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nAno de Publicação: {self.ano_publicacao}\nDisponibilidade: {"Sim" if self.disponibilidade else "Não"}\n'

    def adicionar(self, biblioteca):
        biblioteca.livros.append(self)

    @staticmethod
    def buscar(biblioteca, titulo=None, autor=None):
        resultados = []
        for livro in biblioteca.livros:
            if (titulo and titulo.lower() in livro.titulo.lower()) or (autor and autor.lower() in livro.autor.lower()):
                resultados.append(livro)
        return resultados

    def emprestar(self, usuario):
        if self.disponibilidade:
            self.disponibilidade = False
            usuario.livros_emprestados.append(self)
            print(f'Livro "{self.titulo}" emprestado para {usuario.nome}.')
        else:
            print(f'Livro "{self.titulo}" não está disponível.')

    def devolver(self, usuario):
        if self in usuario.livros_emprestados:
            self.disponibilidade = True
            usuario.livros_emprestados.remove(self)
            print(f'Livro "{self.titulo}" devolvido por {usuario.nome}.')
        else:
            print(f'Este livro não foi emprestado para {usuario.nome}.')

# Classe Autor.
class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f'Nome do Autor: {self.nome}\nNacionalidade: {self.nacionalidade}\n'

# Classe Usuário.
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.livros_emprestados = []

    def __str__(self):
        return f'Nome do Usuário: {self.nome}\nIdade do Usuário: {self.idade}\nLivros Emprestados: {[livro.titulo for livro in self.livros_emprestados]}\n'

# Classe Biblioteca para gerenciar a coleção de livros.
class Biblioteca:
    def __init__(self):
        self.livros = []

# Função principal para o menu.
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            isbn = input("Digite o ISBN: ")
            ano_publicacao = input("Digite o ano: ")
            livro = Livro(titulo, autor, isbn, ano_publicacao)
            livro.adicionar(biblioteca)
            print("Livro adicionado com sucesso.")

        elif escolha == '2':
            titulo = input("Digite o título do livro (ou deixe em branco para buscar por autor): ")
            autor = input("Digite o nome do autor (ou deixe em branco para buscar por título): ")
            resultados = Livro.buscar(biblioteca, titulo, autor)
            if resultados:
                for livro in resultados:
                    print(livro)
            else:
                print("livro não encontrado.")

        elif escolha == '3':
            nome_usuario = input("Digite o nome do usuário: ")
            idade_usuario = input("Digite a idade do usuário: ")
            usuario = Usuario(nome_usuario, idade_usuario)
            titulo = input("Digite o título do livro para emprestar: ")
            resultados = Livro.buscar(biblioteca, titulo=titulo)
            if resultados:
                livro = resultados[0]
                livro.emprestar(usuario)
            else:
                print("Livro não encontrado ou indisponível.")

        elif escolha == '4':
            nome_usuario = input("Digite o nome do usuário: ")
            idade_usuario = input("Digite a idade do usuário: ")
            usuario = Usuario(nome_usuario, idade_usuario)
            titulo = input("Digite o título do livro para devolver: ")
            resultados = Livro.buscar(biblioteca, titulo=titulo)
            if resultados:
                livro = resultados[0]
                livro.devolver(usuario)
            else:
                print("Livro não encontrado ou não emprestado para este usuário.")

        elif escolha == '5':
            print("Encerrando o programa")
            break

        else:
            print("Opção inválida.")
        
menu()
