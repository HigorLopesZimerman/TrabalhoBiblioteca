from modelos.cidade import Cidade
from utils import salvar_registro, ler_registro

ARQUIVOS_CIDADES = "dados/cidades.jsonl"

def main():
    sp = Cidade(1, "São Paulo", "SP")
    salvar_registro(sp.to_dict(), ARQUIVOS_CIDADES)
    
    cidades = ler_registro(ARQUIVOS_CIDADES)
    
    print("cidades cadastradas:")
    for c in cidades:
        print(c)
        
        
    
if __name__ == "__main__":
    main()