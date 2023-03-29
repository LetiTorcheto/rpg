class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque

    def __str__(self):
        return f'O ser vivo possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque'
    
    def atacar(self, individuo):
        try:
            if self.pontos_vida > 0 :
                individuo.pontos_vida -= self.pontos_ataque
                if individuo.pontos_vida <= 0:
                   print("O jogo acabou!") 
            else:
                print("O jogo acabou!")
        except ValueError as error:
            print(error)
