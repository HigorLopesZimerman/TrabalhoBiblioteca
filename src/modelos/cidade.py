
class Cidade:
    def __init__(self, codigo: int, nome: str, estado: str):
        self.codigo = codigo
        self.nome = nome
        self.estado = estado
        
        
    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "estado": self.estado
        }
        
    def from_dict(data: dict):
        return Cidade(data["codigo"], data["nome"], data["estado"])