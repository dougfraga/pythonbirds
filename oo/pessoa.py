class Pessoa:
    olhos = 2

    def __init__(self, nome=None, idade=30, *filhos):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        return f'{super().cumprimentar()} Show!'



if __name__ == '__main__':
    doug = Homem('Doug', 37, 'Flor', 'Maju')
    braaw = Pessoa('Nilton', 70, doug)
    for filho in braaw.filhos:
        print(filho.nome)
        print(Pessoa.nome_e_atributos_de_classe())
    print(braaw.cumprimentar())
