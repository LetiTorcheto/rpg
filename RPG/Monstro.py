from Ser_vivo import SerVivo

class Monstro(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, tipo):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

    def  chama_monstro(self):
        return f'Pontos de vida: {self.pontos_vida} \nPontos de ataque: {self.pontos_ataque} \nTipo: {self.tipo}'