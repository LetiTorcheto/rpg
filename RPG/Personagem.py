from Ser_vivo import SerVivo

class Personagem(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

    def chama_personagem(self):
        return f'Nome: {self.nome} \nPontos de vida: {self.pontos_vida} \nPontos de ataque: {self.pontos_ataque}'