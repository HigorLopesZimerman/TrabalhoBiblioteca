


class Emprestimo:
    def __init__(self, codigo: int, cod_livro: int, cod_aluno: int, data_emprestimo: str, data_devolucao: str, devolvido: str = "Não"):
        self.codigo = codigo
        self.cod_livro = cod_livro
        self.cod_aluno = cod_aluno
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.devolvido = devolvido  # sim ou nao

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "cod_livro": self.cod_livro,
            "cod_aluno": self.cod_aluno,
            "data_emprestimo": self.data_emprestimo,
            "data_devolucao": self.data_devolucao,
            "devolvido": self.devolvido
        }

    @staticmethod
    def from_dict(data: dict):
        return Emprestimo(
            codigo=data["codigo"],
            cod_livro=data["cod_livro"],
            cod_aluno=data["cod_aluno"],
            data_emprestimo=data["data_emprestimo"],
            data_devolucao=data["data_devolucao"],
            devolvido=data.get("devolvido", "Não")
        )

    def __str__(self):
        return f"Empréstimo {self.codigo}: Livro {self.cod_livro}, Aluno {self.cod_aluno}, Devolvido: {self.devolvido}"
