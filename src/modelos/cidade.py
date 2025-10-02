class Cidade:
    def __init__(self, codigo: int, descricao: str, estado: str):
        self.codigo = codigo
        self.descricao = descricao
        self.estado = estado

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "descricao": self.descricao,
            "estado": self.estado
        }

    @staticmethod
    def from_dict(data: dict):
        return Cidade(
            codigo=data["codigo"],
            descricao=data["descricao"],
            estado=data["estado"]
        )

    def __str__(self):
        return f"Cidade {self.codigo}: {self.descricao}/{self.estado}"
