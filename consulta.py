class Consulta:
    def __init__(self, codigo, codigo_paciente, data, especialidade, medico, diagnostico=""):
        self.codigo = codigo
        self.codigo_paciente = codigo_paciente
        self.data = data
        self.especialidade = especialidade
        self.medico = medico
        self.diagnostico = diagnostico

    def atualizar(self, data=None, especialidade=None, medico=None, diagnostico=None):
        if data:
            self.data = data
        if especialidade:
            self.especialidade = especialidade
        if medico:
            self.medico = medico
        if diagnostico:
            self.diagnostico = diagnostico  # Permitir atualização do diagnóstico

    def __repr__(self):
        return f'\nCÓDIGO DA CONSULTA = {self.codigo}, CÓDIGO DO PACIENTE = {self.codigo_paciente}, DATA = {self.data}, ESPECIALIDADE = {self.especialidade}, MÉDICO = {self.medico}, DIAGNÓSTICO = {self.diagnostico}'
