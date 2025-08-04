def main():
    import argparse
    from desafio2.app.logic import escolher_garrafas

    parser = argparse.ArgumentParser()
    parser.add_argument("--galao", type=float, help="Volume do galão")
    parser.add_argument("--garrafa", type=float, action="append", help="Volume das garrafas")
    args = parser.parse_args()

    if args.galao and args.garrafa:
        resultado, sobra = escolher_garrafas(args.galao, args.garrafa)
        print(f"Garrafas usadas: {resultado}, Sobra: {sobra}")
    else:
        volume_galao = float(input("Insira o volume do galão: "))
        garrafas = list(map(float, input("Insira os volumes das garrafas separados por espaço: ").split()))
        resultado, sobra = escolher_garrafas(volume_galao, garrafas)
        print(f"Garrafas usadas: {resultado}, Sobra: {sobra}")

if __name__ == "__main__":
    main()