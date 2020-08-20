class Pessoa:
    def __init__(self, nome=None, idade=36):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'


if __name__ == '__main__':
    p = Pessoa('Doug', 37)
    print(p.cumprimentar())
