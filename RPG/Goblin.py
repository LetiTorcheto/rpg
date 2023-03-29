from Monstro import Monstro

class Goblin(Monstro):

    def __init__(self, pontos_vida, pontos_ataque, tipo, inteligencia):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.inteligencia = inteligencia

    def chama_goblim(self):
        return f'Pontos de vida: {self.pontos_vida} \nPontos de ataque: {self.pontos_ataque} \nInteligencia: {self.inteligencia}\nTipo: {self.tipo}.'
