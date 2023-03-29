from Monstro import Monstro

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, tipo, forca):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.forca = forca

    def chama_lobo(self):
        return f'Pontos de vida: {self.pontos_vida} \nPontos de ataque: {self.pontos_ataque} \n Força:{self.forca} \n Tipo: {self.tipo}.'
