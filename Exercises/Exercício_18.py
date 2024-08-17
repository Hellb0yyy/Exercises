import random

def lancar_moeda():
    resultado = random.choice(['Cara', 'Coroa'])
    return resultado

resultado = lancar_moeda()
print(f"O resultado do lançamento da moeda é: {resultado}")
