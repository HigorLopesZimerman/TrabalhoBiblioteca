from autor import Autor
from categoria import Categoria

class Livro:
    def __init__(self, codigo: int, titulo: str, autor: Autor, categoria: Categoria, ano_publicacao: int, disponivel: bool):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel