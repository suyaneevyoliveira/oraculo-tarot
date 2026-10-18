"""Funções de sorteio: aleatórias e sem reposição dentro de cada baralho."""
import random

def sortear_cartas(baralho, quantidade, permitir_inversoes=False):
    if quantidade < 1:
        raise ValueError("A quantidade precisa ser pelo menos 1.")
    if quantidade > len(baralho):
        raise ValueError(f"Esse baralho tem somente {len(baralho)} cartas.")
    selecionadas = random.SystemRandom().sample(baralho, quantidade)
    resultado = []
    rng = random.SystemRandom()
    for carta in selecionadas:
        item = dict(carta)
        item["orientacao"] = (
            "Invertida" if permitir_inversoes and rng.random() < 0.5 else "Normal"
        )
        if item["baralho"] == "Baralho Cigano":
            item["orientacao"] = "Normal"
        resultado.append(item)
    return resultado
