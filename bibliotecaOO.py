#classe Livro.
class Livros():
    #parametros para a classe.
    def __init__(self, id, titulo, autor, ISBN, ano_publicacao, disponibilidade) :
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = ISBN
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade

    #retorna os dados inseridos nos parametros.
    def __str__(self) :
        return f'ID: {self._id}\n Nome: {self._nome}\n Autor: {self._autor}\n ISBN: {self._isbn}\n Ano De Publicação: {self._ano_publicacao}\n Disponibilidade: {self._disponibilidade}\n'

    def get_livro(self):
        pass

    def set_livro(self):
        pass

#classe de autores.
class Autores :
    #parametros.
    def __init__(self, nome, nacionalidade) :
        self.nome = nome
        self.nacionalidade = nacionalidade

    #retorna os dados inseridos nos parametros.    
    def __str__(self) :
        return f'Nome autor: {self._nome} \n Nacionalidade: {self._nacionalidade}\n'
    
    #"retorna" um autor.
    def get_autor(self) :
        return self._nome, self._nacionalidade

    #adicionar um autor.
    def set_autor(self, nome, nacionalidade) :
        self._nome = nome
        self._nacionalidade = nacionalidade

#classe de Usuários.
class Usuarios() :
    #parametros.
    def __init__ (self, id, nome, idade) :
        self.id = id
        self.nome = nome
        self.idade = idade

    #retorna os dados inseridos nos parametros.    
    def __str__ (self) :
        return f'ID do Usuário: {self._nome}\n Nome do Usuário: {self._nome}\n Idade do Usuário: {self._idade}\n'
    
    #"retorna" um usuário.
    def get_usuario(self) :
        pass

    #adicionar um usuário.
    def set_usuario(self, id, nome, idade) :
        self._id = id
        self._nome = nome
        self._idade = idade

def add_livro(Livros) :
    print ("-----adicionar livro-----")
    