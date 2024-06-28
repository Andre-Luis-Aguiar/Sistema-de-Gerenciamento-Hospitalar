from paciente import Paciente
from consulta import Consulta
from prontuario import Prontuario
from dados import salvar_dados, carregar_dados

PACIENTES_ARQUIVO = 'data/pacientes.pkl'
CONSULTAS_ARQUIVO = 'data/consultas.pkl'
PRONTUARIOS_ARQUIVO = 'data/prontuarios.pkl'


pacientes = []
consultas = []
prontuarios = []

def carregar_todos_os_dados():
    global pacientes, consultas, prontuarios
    pacientes = carregar_dados(PACIENTES_ARQUIVO)
    consultas = carregar_dados(CONSULTAS_ARQUIVO)
    prontuarios = carregar_dados(PRONTUARIOS_ARQUIVO)

def salvar_todos_os_dados():
    salvar_dados(PACIENTES_ARQUIVO, pacientes)
    salvar_dados(CONSULTAS_ARQUIVO, consultas)
    salvar_dados(PRONTUARIOS_ARQUIVO, prontuarios)

def menu():
    while True:
        print("\nMenu:")
        print("1. Gerenciar Pacientes")
        print("2. Gerenciar Consultas")
        print("3. Gerenciar Prontuários")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            gerenciar_pacientes()
        elif escolha == '2':
            gerenciar_consultas()
        elif escolha == '3':
            gerenciar_prontuarios()
        elif escolha == '0':
            
                        break
        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_pacientes():
    while True:
        print("\nGerenciar Pacientes:")
        print("1. Cadastrar Paciente")
        print("2. Alterar Paciente")
        print("3. Excluir Paciente")
        print("4. Consultar Paciente")
        print("5. Listar Pacientes")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_paciente()
        elif escolha == '2':
            alterar_paciente()
        elif escolha == '3':
            excluir_paciente()
        elif escolha == '4':
            consultar_paciente()
        elif escolha == '5':
            listar_pacientes()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_paciente():
    codigo = input("Código: ")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    genero = input("Gênero: ")

    paciente = Paciente(codigo, nome, cpf, idade, genero)
    pacientes.append(paciente)
    prontuario = Prontuario(paciente)
    prontuarios.append(prontuario)
    print("Paciente cadastrado com sucesso!")
    salvar_todos_os_dados()


def alterar_paciente():
    codigo = input("Código do paciente a ser alterado: ")
    paciente = localizar_entidade(pacientes, codigo)
    if paciente:
        nome = input("Novo nome (deixe em branco para não alterar): ")
        cpf = input("Novo CPF (deixe em branco para não alterar): ")
        idade = input("Nova idade (deixe em branco para não alterar): ")
        genero = input("Novo gênero (deixe em branco para não alterar): ")
        paciente.atualizar(nome=nome if nome else None, cpf=cpf if cpf else None, idade=int(idade) if idade else None, genero=genero if genero else None)
        print("Paciente atualizado com sucesso!")
        salvar_todos_os_dados()        
    else:
        print("Paciente não encontrado.")

def excluir_paciente():
    codigo = input("Código do paciente a ser excluído: ")
    paciente = localizar_entidade(pacientes, codigo)
    if paciente:
        pacientes.remove(paciente)
        prontuario = localizar_prontuario(codigo)
        if prontuario:
            for consulta in prontuario.consultas:
                consultas.remove(consulta)
            prontuarios.remove(prontuario)
        print("Paciente e registros relacionados excluídos com sucesso!")
        salvar_todos_os_dados()
    else:
        print("Paciente não encontrado.")

def consultar_paciente():
    codigo = input("Código do paciente: ")
    paciente = localizar_entidade(pacientes, codigo)
    if paciente:
        print(paciente)
    else:
        print("Paciente não encontrado.")

def listar_pacientes():
   print(f"\n\nTotal de pacientes: {len(pacientes)}")
   for paciente in pacientes:
        print(paciente)
        
def gerenciar_consultas():
    while True:
        print("\nGerenciar Consultas:")
        print("1. Agendar Consulta")
        print("2. Alterar Consulta")
        print("3. Cancelar Consulta")
        print("4. Consultar Consulta")
        print("5. Listar Consultas")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            agendar_consulta()
        elif escolha == '2':
            alterar_consulta()
        elif escolha == '3':
            cancelar_consulta()
        elif escolha == '4':
            consultar_consulta()
        elif escolha == '5':
            listar_consultas()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def agendar_consulta():
    codigo = input("Código da consulta: ")
    codigo_paciente = input("Código do paciente: ")
    paciente = localizar_entidade(pacientes, codigo_paciente)
    if not paciente:
        print("Paciente não encontrado.")
        return

    data = input("Data da consulta (DD-MM-AAAA): ")
    especialidade = input("Especialidade da consulta (Ex: Dermatológica): ")
    medico = input("Nome do médico: ")
    diagnostico = input("Diagnóstico preliminar (opcional): ")

    consulta = Consulta(codigo, codigo_paciente, data, especialidade, medico, diagnostico)
    consultas.append(consulta)

    prontuario = localizar_prontuario(codigo_paciente)
    if not prontuario:
        prontuario = Prontuario(paciente)
        prontuarios.append(prontuario)
    prontuario.adicionar_consulta(consulta)

    print("Consulta agendada com sucesso!")
    salvar_todos_os_dados()

def alterar_consulta():
    codigo = input("Código da consulta a ser alterada: ")
    consulta = localizar_entidade(consultas, codigo)
    if consulta:
        data = input("Nova data (deixe em branco para não alterar): ")
        especialidade = input("Nova especialidade (deixe em branco para não alterar): ")
        medico = input("Novo médico (deixe em branco para não alterar): ")
        diagnostico = input("Novo diagnóstico (deixe em branco para não alterar): ")
        consulta.atualizar(data=data if data else None, especialidade=especialidade if especialidade else None, medico=medico if medico else None, diagnostico=diagnostico if diagnostico else None)
        print("Consulta atualizada com sucesso!")
        salvar_todos_os_dados()     
    else:
        print("Consulta não encontrada.")

def cancelar_consulta():
    codigo = input("Código da consulta a ser cancelada: ")
    consulta = localizar_entidade(consultas, codigo)
    if consulta:
        consultas.remove(consulta)
        print("Consulta cancelada com sucesso!")
    else:
        print("Consulta não encontrada.")

def consultar_consulta():
    codigo = input("Código da consulta: ")
    consulta = localizar_entidade(consultas, codigo)
    if consulta:
        print(consulta)
    else:
        print("Consulta não encontrada.")

def listar_consultas():
    print(f"\n\nTotal de consultas agendadas: {len(consultas)}")
    for consulta in consultas:
        print(consulta)

def gerenciar_prontuarios():
    while True:
        print("\nGerenciar Prontuários:")
        print("1. Adicionar Registro ao Prontuário")
        print("2. Consultar Prontuário")
        print("3. Listar Prontuários")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_registro_prontuario()
        elif escolha == '2':
            consultar_prontuario()
        elif escolha == '3':
            listar_prontuarios()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_registro_prontuario():
    codigo_paciente = input("Código do paciente: ")
    consulta_codigo = input("Código da consulta a ser adicionada ao prontuário: ")
    
    consulta = localizar_entidade(consultas, consulta_codigo)
    if not consulta:
        print("Consulta não encontrada.")
        return

    prontuario = localizar_prontuario(codigo_paciente)
    if not prontuario:
        print(f"Prontuário não encontrado para o paciente com código {codigo_paciente}. Criando novo prontuário.")
        prontuario = Prontuario(codigo_paciente)
        prontuarios.append(prontuario)
    
    prontuario.adicionar_consulta(consulta)
    print("Registro adicionado ao prontuário com sucesso!")
    salvar_todos_os_dados()

def consultar_prontuario():
    codigo_paciente = input("Código do paciente: ")
    prontuario = localizar_prontuario(codigo_paciente)
    if prontuario:
        print(prontuario)
    else:
        print(f"Prontuário não encontrado para o paciente com código {codigo_paciente}.")

def consultar_prontuario():
    codigo_paciente = input("Código do paciente: ")
    prontuario = localizar_prontuario(codigo_paciente)
    if prontuario:
        print(prontuario)
    else:
        print(f"Prontuário não encontrado para o paciente com código {codigo_paciente}.")

def listar_prontuarios():
    print(f"Total de prontuários: {len(prontuarios)}")
    for prontuario in prontuarios:
        print(prontuario)

def localizar_entidade(entidades, codigo):
    for entidade in entidades:
        if entidade.codigo == codigo:
            return entidade
    return None

def localizar_prontuario(codigo_paciente):
    for prontuario in prontuarios:
        if prontuario.paciente.codigo == codigo_paciente:
            return prontuario
    return None

if __name__ == "__main__":
    carregar_todos_os_dados()
    menu()

