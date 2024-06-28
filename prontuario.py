class Prontuario:
    def __init__(self, paciente):
        self.paciente = paciente
        self.consultas = []

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def __repr__(self):
        consultas_info = "\n".join([str(consulta) for consulta in self.consultas])
        return f'\nPACIENTE: {self.paciente.nome}, CÓDIGO: {self.paciente.codigo}, CONSULTAS:\n{consultas_info}'