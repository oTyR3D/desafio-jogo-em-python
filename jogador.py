class Jogador:
    def __init__(self, nome="Jogador", vida=100, armadura=10, forca=15, esmeraldas=0):
        self.nome = nome
        self.vida = vida
        self.armadura = armadura
        self.forca = forca
        self.esmeraldas = esmeraldas
        self.inventario = {"poção de vida": 0, "poção de força": 0}

    def get_nome(self):
        self.nome = input("Qual o nome do Jogador?\n").strip()

    def status(self):
        print(f"""Status de {self.nome}:
    Vida: {self.vida}
    Armadura: {self.armadura}
    Força: {self.forca}
    Esmeraldas: {self.esmeraldas}""")

    def mostrar_inventario(self):
        print("\nInventário:")
        for i, (item, qtd) in enumerate(self.inventario.items(), 1):
            print(f"{i}. {item}: {qtd}")

    def usar_item(self):
        self.mostrar_inventario()
        try:
            opcao = int(input("\nQual item deseja usar? ")) - 1
            item = list(self.inventario.keys())[opcao]

            if self.inventario[item] <= 0:
                print("Você não tem mais deste item!")
                return

            if item == "poção de vida":
                self.vida += 30
                print("+30 de vida!")
            elif item == "poção de força":
                self.forca += 15
                print("+15 de força!")

            self.inventario[item] -= 1
        except (IndexError, ValueError):
            print("Opção inválida!")

    def adicionar_item(self, item, quantidade=1):
        if item in self.inventario:
            self.inventario[item] += quantidade
        else:
            self.inventario[item] = quantidade

        if item == "esmeralda":
            self.esmeraldas += quantidade
