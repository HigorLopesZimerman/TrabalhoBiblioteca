class Livro:
    def __init__(self, codigo: int, titulo: str, cod_autor: int, cod_categoria: int,
                 ano_publicacao: int, disponibilidade: str = "disponível"):
        self.codigo = codigo
        self.titulo = titulo
        self.cod_autor = cod_autor
        self.cod_categoria = cod_categoria
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade 

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "cod_autor": self.cod_autor,
            "cod_categoria": self.cod_categoria,
            "ano_publicacao": self.ano_publicacao,
            "disponibilidade": self.disponibilidade
        }

    @staticmethod
    def from_dict(data: dict):
        return Livro(
            codigo=data["codigo"],
            titulo=data["titulo"],
            cod_autor=data["cod_autor"],
            cod_categoria=data["cod_categoria"],
            ano_publicacao=data["ano_publicacao"],
            disponibilidade=data.get("disponibilidade", "disponível")
        )

    def __str__(self):
        return f"Livro {self.codigo}: {self.titulo} ({self.ano_publicacao}) - {self.disponibilidade}"
