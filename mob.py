from auxilio import RNG

class Mob:
    def __init__(self, rodada):
        self.lista_tipos_mobs = ['aranha', 'zumbi', 'IRON GOLEM']

        # Chefe a cada 10 rodadas
        if rodada % 10 == 0 and rodada != 0:
            self.tipo = self.lista_tipos_mobs[2]
            self.vida = 150
            self.forca = 40
            print("\nUM IRON GOLEM APARECEU! CUIDADO!")
        else:
            self.tipo = self.lista_tipos_mobs[0] if RNG() > 50 else self.lista_tipos_mobs[1]
            self.vida = 40 if self.tipo == 'aranha' else 60
            self.forca = 20 if self.tipo == 'aranha' else 30
            print(f'\nUm {self.tipo} apareceu!')

        self.get_status()

    def get_status(self):
        print(f"{self.tipo} - Vida: {self.vida}, Força: {self.forca}")

    def gerarDrop(self):
        if self.tipo == 'IRON GOLEM':
            print("O IRON GOLEM deixou cair 3 esmeraldas!")
            return "esmeralda", 3

        if RNG() > 60:
            return "poção de vida", 1
        elif RNG() > 30:
            return "poção de força", 1

        return None, 0
