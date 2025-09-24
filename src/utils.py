import json
import os

def salvar_registro(obj: dict, arquivo: str):
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
        
def ler_registro(arquivo: str):
    registros = []
    if not os.path.exists(arquivo):
        return registros
    
    
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            registros.append(json.loads(linha))
        return registros