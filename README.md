# 🟩 Minecraft Simples em Python ⛏️

Um pequeno jogo de RPG por turnos, inspirado na estética e nos mobs do universo Minecraft — feito inteiramente em Python para terminal!

## 🎮 Como Jogar

Você enfrentará **mobs aleatórios** como Aranhas, Zumbis e até o temido IRON GOLEM! A cada rodada, escolha entre:

- ⚔️ **Atacar**: Tente causar dano com chance de acerto baseada em sua força e vida.
- 🧪 **Usar item**: Recupere vida ou ganhe mais força.
- 🏃‍♂️ **Fugir**: 70% de chance de escapar do combate.

### 🧠 Mecânicas de Combate

- **Chance de acerto**: Começa em 40% e sobe até 100% dependendo da força + vida.
- **Crítico do jogador**: 10% de chance (dano dobrado).
- **Crítico dos mobs**: 5% de chance.
- **Todos podem errar!** 👀

## 📦 Estrutura do Projeto

```bash
.
├── main.py        # Jogo principal
├── jogador.py     # Classe do jogador
├── mob.py         # Mobs inimigos
├── auxilio.py     # Funções utilitárias (RNG, limpar tela)
