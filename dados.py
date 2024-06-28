import pickle
import os

def salvar_dados(arquivo, dados):
    with open(arquivo, 'wb') as f:
        pickle.dump(dados, f)

def carregar_dados(arquivo):
    if not os.path.exists(arquivo) or os.path.getsize(arquivo) == 0:
        return []
    try:
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    except EOFError:
        return []
