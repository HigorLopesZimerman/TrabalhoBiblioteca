class Categoria:
    def __init__(self, codigo: int, descricao: str):
        self.codigo = codigo
        self.descricao = descricao

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "descricao": self.descricao
        }

    @staticmethod
    def from_dict(data: dict):
        return Categoria(
            codigo=data["codigo"],
            descricao=data["descricao"]
        )

    def __str__(self):
        return f"Categoria {self.codigo}: {self.descricao}"
