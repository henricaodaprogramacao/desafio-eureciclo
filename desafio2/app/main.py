from desafio2.app.logic import escolher_garrafas

def main():
    volume_galao = float(input("Insira o volume do galão: "))
    qtd_garrafas = int(input("Quantidade de garrafas: "))

    garrafas = []
    for i in range(qtd_garrafas):
        volume = float(input(f"Garrafa {i + 1}: "))
        garrafas.append(volume)

    combinacao, sobra = escolher_garrafas(volume_galao, garrafas)

    print(f"Resposta: {combinacao}, sobra {sobra:.1f}L")

if __name__ == "__main__":
    main()