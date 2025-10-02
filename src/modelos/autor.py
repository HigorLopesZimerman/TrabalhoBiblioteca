class Autor:
    def __init__(self, codigo: int, nome: str, cod_cidade: int):
        self.codigo = codigo
        self.nome = nome
        self.cod_cidade = cod_cidade

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "cod_cidade": self.cod_cidade
        }

    @staticmethod
    def from_dict(data: dict):
        return Autor(
            codigo=data["codigo"],
            nome=data["nome"],
            cod_cidade=data["cod_cidade"]
        )

    def __str__(self):
        return f"Autor {self.codigo}: {self.nome} (Cidade: {self.cod_cidade})"
