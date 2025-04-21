# nome, vida, armadura, força, inventario(lista), esmeraldas
# status, adicionar item, usar item, atacar -> mob

class Jogador:
    def __init__(self, nome, vida, armadura, forca, inventario, esmeraldas):
        self.nome = nome
        self.vida = vida
        self.armadura = armadura
        self.forca = forca
        self.inventario = inventario
        self.esmeraldas = esmeraldas
        self.inventario = ['roupa','blusa']

    def get_nome(self):
        self.nome=input("Qual o nome de Jogador?\n")

    def status (self):
        print(f"""O Jogador {self.nome} possui:
    {self.vida} de vida
    {self.armadura} de armadura
    {self.forca} de força
    {self.esmeraldas} esmeraldas""")

    def mostrar_inventario(self):
        for x,self.inventario in enumerate(self.inventario):
            print(f"{x+1}-{self.inventario}")


    def usar_item(self):
        pass

