class Pessoa:
    olhos = 2

    def __init__(self, nome=None, idade=30, *filhos):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'


if __name__ == '__main__':
    doug = Pessoa('Doug', 37, 'Flor', 'Maju')
    braaw = Pessoa('Nilton', 70, doug)
    for filho in braaw.filhos:
        print(filho.nome)
