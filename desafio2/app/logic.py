from itertools import combinations

def escolher_garrafas(galao, garrafas):
    melhor_combinacao = None
    menor_sobra_total = float('inf')
    menor_qtd = float('inf')

    for r in range(1, len(garrafas) + 1):
        for combo in combinations(garrafas, r):
            volume_combo = sum(combo)
            if volume_combo >= galao:
                sobra_total = volume_combo - galao
                if (
                    sobra_total < menor_sobra_total
                    or (sobra_total == menor_sobra_total and len(combo) < menor_qtd)
                ):
                    melhor_combinacao = combo
                    menor_sobra_total = sobra_total
                    menor_qtd = len(combo)

    # Caso não encontre nenhuma combinação maior ou igual ao galão
    if melhor_combinacao is None:
        melhor_combinacao = max(garrafas, key=lambda x: x)  # pega a maior garrafa
        return [melhor_combinacao], round(melhor_combinacao - galao, 6)

    return sorted(melhor_combinacao), round(menor_sobra_total, 6)
