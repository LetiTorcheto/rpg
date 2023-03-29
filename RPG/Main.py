from Ser_vivo import SerVivo
from Personagem import Personagem
from Monstro import Monstro
from Lobo import Lobo
from Goblin import Goblin


ser_vivo = SerVivo(pontos_vida=60, pontos_ataque=50)
personagem = Personagem(pontos_vida=60, pontos_ataque=50, nome="Heroi")
monstro = Monstro(pontos_vida=55, pontos_ataque=50, tipo='Dragão')
lobo_n1 = Lobo(pontos_vida=30, pontos_ataque=25, tipo='Nivel 1', forca=20)
gob_n1 = Goblin(pontos_ataque=20,pontos_vida=35,inteligencia=20, tipo="Goblin")



personagem.atacar(ser_vivo)
print(ser_vivo)

personagem.atacar(lobo_n1)
print(lobo_n1)

personagem.atacar(monstro)
print(monstro)

personagem.atacar(gob_n1)
print(gob_n1)

