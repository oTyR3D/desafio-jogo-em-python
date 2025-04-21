# nome, vida, armadura, força, inventario(lista), esmeraldas
# status, adicionar item, usar item, atacar -> mob

class Jogador:
    def __init__(self):
        self.nome = None
        self.vida = 10
        self.armadura = 5
        self.forca = 5
        self.esmeraldas = 0
        self.inventario = {"poção de vida":0,"poção de força":0}

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
        self.mostrar_inventario()
        x=int(input('Qual item deseja usar?'))-1
        if x==0:
            print("Curando em 10 pontos de vida")
            self.vida+=10
        else:
            print("Aumento de força em 10 pontos")

    def adicionar_item(self,item):
        if
