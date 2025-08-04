from itertools import combinations

def escolher_garrafas(galao, garrafas):
    melhor_combinacao = None
    menor_sobra_total = float('inf')
    menor_qtd = float('inf')

    for r in range(1, len(garrafas)+1):
        for combo in combinations(garrafas, r):
            usados = []
            volume_atual = 0

            for i, g in enumerate(combo):
                if volume_atual + g <= galao:
                    usados.append(g)
                    volume_atual += g
                else:
                    restante = galao - volume_atual
                    if restante > 0:
                        usados.append(restante)
                        volume_atual += restante
                    break

            if round(volume_atual, 6) == galao:
                sobra_total = sum(combo) - galao  # quanto sobrou nas garrafas
                if sobra_total < menor_sobra_total or (
                    sobra_total == menor_sobra_total and len(combo) < menor_qtd
                ):
                    melhor_combinacao = combo
                    menor_sobra_total = sobra_total
                    menor_qtd = len(combo)

    return sorted(melhor_combinacao), round(menor_sobra_total, 6)