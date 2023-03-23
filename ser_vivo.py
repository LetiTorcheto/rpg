
#classe ser vivo  = vida, ataque
#classe personagem = nome 
#classe monstro = tipo
#   classe lobo(derivada de monstro) = inteligencia
#   classe goblin(derivada de monstro) = força

# a cada rodada que acontecer o status deve ser impresso na tela

class Ser_vivo: 
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
    # O dano vai para o mmonstro
    def atacar_monstro(self):
        if gob_n1.pontos_vida > 0 :
            self.dano = personagem.pontos_ataque
            self.oponente_atacado = gob_n1.pontos_vida
            gob_n1.pontos_vida = self.oponente_atacado - self.dano
        else:
            print("O jogo acabou!")
    #o dano vai para o personagem
    
    def atacar_personagem(self):
        if self.pontos_vida > 0 :
            self.dano = gob_n1.pontos_ataque
            self.oponente_atacado = personagem.pontos_vida
            personagem.pontos_vida = self.oponente_atacado - self.dano
        else:
            print("O jogo acabou!") 
            


    def chama_Personagem(self):
        print(personagem.nome)

    def chama_monstro(self):
        print(gob_n1.tipo)

    def status(self):
        print("Vida atual:", self.pontos_vida)
    
class Personagem(Ser_vivo):
    def __init__(self,pontos_vida, pontos_ataque,nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome
    

class Monstro (Ser_vivo):
     def __init__(self, pontos_vida, pontos_ataque,tipo):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

    
class Lobo(Monstro):
     def __init__(self, pontos_vida, pontos_ataque, tipo, forca):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.forca = forca
        

class Goblin(Monstro):
     def __init__(self, pontos_vida, pontos_ataque, inteligencia, tipo):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.inteligencia = inteligencia


personagem = Personagem(pontos_vida=60, pontos_ataque=20, nome="Heroi")
personagem.chama_Personagem()
personagem.status()

gob_n1 = Goblin(pontos_ataque=20,pontos_vida=35,inteligencia=20, tipo="Goblin")
gob_n1.chama_monstro()
gob_n1.status()

personagem.atacar_monstro()

gob_n1.chama_monstro()
gob_n1.status()

gob_n1.atacar_personagem()

personagem.chama_Personagem()
personagem.status()

personagem.atacar_monstro()

gob_n1.chama_monstro()
gob_n1.status()

gob_n1.atacar_personagem()

personagem.chama_Personagem()
personagem.status()



