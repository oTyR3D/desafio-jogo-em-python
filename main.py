from auxilio import RNG
from jogador import Jogador
from mob import Mob

def chance(forca, vida):
    return min(100, 40 + int((forca + vida) * 0.2))

def ataque(atk, vida, forca, alvo_vida, armadura=0, crit=10):
    if RNG() <= chance(forca, vida):
        dano = max(1, forca - armadura)
        if RNG() <= crit:
            dano *= 2
        alvo_vida -= dano
        print(f"{atk} acertou {'CRÍTICO! ' if dano > forca else ''}Dano: {dano}")
    else:
        print(f"{atk} errou!")
    return alvo_vida

def combate(jogador, mob):
    while jogador.vida > 0 and mob.vida > 0:
        print("\n1. Atacar\n2. Usar item\n3. Fugir")
        esc = input().strip()

        if esc == "1":
            mob.vida = ataque("Você", jogador.vida, jogador.forca, mob.vida)
            if mob.vida <= 0:
                print(f"Derrotou o {mob.tipo}!")
                i, q = mob.gerarDrop()
                if i: jogador.adicionar_item(i, q)
                return True
            jogador.vida = ataque(mob.tipo, mob.vida, mob.forca, jogador.vida, jogador.armadura, 5)
        elif esc == "2":
            jogador.usar_item()
        elif esc == "3":
            if RNG() > 30:
                print("Fugiu!")
                return False
            print("Falhou! Inimigo ataca!")
            jogador.vida = ataque(mob.tipo, mob.vida, mob.forca, jogador.vida, jogador.armadura, 5)

        print(f"Vida: {jogador.vida}")
        mob.get_status()

def main():
    from auxilio import limparTela
    limparTela()
    print("=== Jogo de Minecraft Simples ===")
    jogador = Jogador()
    jogador.get_nome()

    rodada = 1
    while jogador.vida > 0:
        print(f"\n=== Rodada {rodada} ===")
        input("Pressione Enter para encontrar um inimigo...")
        limparTela()

        mob = Mob(rodada)
        if not combate(jogador, mob):
            break

        rodada += 1
        jogador.status()

        if rodada % 10 == 0:
            input("\nPressione Enter para continuar para a próxima fase...")
            limparTela()

    print("\n=== Fim de Jogo ===")
    print(f"Você sobreviveu por {rodada} rodadas!")
    jogador.status()

if __name__ == "__main__":
    main()
