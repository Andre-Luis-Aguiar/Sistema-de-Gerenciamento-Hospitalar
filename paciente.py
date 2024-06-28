class Paciente:
    def __init__(self, codigo, nome, cpf, idade, genero):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.genero = genero
        
    def atualizar(self, nome=None, cpf=None, idade=None, genero=None):
        if nome:
            self.nome = nome
        if cpf:
            self.cpf = cpf
        if idade:
            self.idade = idade
        if genero:
            self.genero = genero

    def __repr__(self):
        return f'\nCÓDIGO = {self.codigo}\nNOME = {self.nome}\nCPF = {self.cpf}\nIDADE = {self.idade}\nGÊNERO = {self.genero}\n'

