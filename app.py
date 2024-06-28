import streamlit as st
from paciente import Paciente
from consulta import Consulta
from prontuario import Prontuario
from dados import salvar_dados, carregar_dados

# Carregar dados salvos
def carregar_todos_os_dados():
    global pacientes, consultas, prontuarios
    pacientes = carregar_dados('data/pacientes.pkl')
    consultas = carregar_dados('data/consultas.pkl')
    prontuarios = carregar_dados('data/prontuarios.pkl')

def salvar_todos_os_dados():
    salvar_dados('data/pacientes.pkl', pacientes)
    salvar_dados('data/consultas.pkl', consultas)
    salvar_dados('data/prontuarios.pkl', prontuarios)

carregar_todos_os_dados()

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

# Funções de manipulação de Pacientes
def cadastrar_paciente(codigo, nome, cpf, idade, genero):
    novo_paciente = Paciente(codigo, nome, cpf, int(idade), genero)
    pacientes.append(novo_paciente)
    novo_prontuario = Prontuario(novo_paciente)
    prontuarios.append(novo_prontuario)
    salvar_todos_os_dados()
    st.success('Paciente cadastrado com sucesso!')

def alterar_paciente(codigo, nome, cpf, idade, genero):
    paciente = localizar_entidade(pacientes, codigo)
    if paciente:
        if nome:
            paciente.nome = nome
        if cpf:
            paciente.cpf = cpf
        if idade:
            paciente.idade = int(idade)
        if genero:
            paciente.genero = genero
        salvar_todos_os_dados()
        st.success('Paciente atualizado com sucesso!')
    else:
        st.error('Paciente não encontrado.')

def excluir_paciente(codigo):
    paciente = localizar_entidade(pacientes, codigo)
    if paciente:
        pacientes.remove(paciente)
        prontuario = localizar_prontuario(codigo)
        if prontuario:
            prontuarios.remove(prontuario)
        salvar_todos_os_dados()
        st.success('Paciente excluído com sucesso!')
    else:
        st.error('Paciente não encontrado.')

def consultar_paciente(codigo):
    paciente = localizar_entidade(pacientes, codigo)
    if paciente:
        st.write(f'Código: {paciente.codigo}')
        st.write(f'Nome: {paciente.nome}')
        st.write(f'CPF: {paciente.cpf}')
        st.write(f'Idade: {paciente.idade}')
        st.write(f'Gênero: {paciente.genero}')
    else:
        st.error('Paciente não encontrado.')

def listar_pacientes():
    if pacientes:
        for paciente in pacientes:
            st.text(str(paciente))
    else:
        st.write("Nenhum paciente cadastrado.")

# Funções de manipulação de Consultas
def agendar_consulta(codigo, codigo_paciente, data, especialidade, medico, diagnostico):
    paciente = localizar_entidade(pacientes, codigo_paciente)
    if not paciente:
        st.error("Paciente não encontrado.")
        return
    nova_consulta = Consulta(codigo, codigo_paciente, data, especialidade, medico, diagnostico)
    consultas.append(nova_consulta)

    prontuario = localizar_prontuario(codigo_paciente)
    if not prontuario:
        prontuario = Prontuario(paciente)
        prontuarios.append(prontuario)
    prontuario.adicionar_consulta(nova_consulta)

    salvar_todos_os_dados()
    st.success('Consulta agendada com sucesso!')

def alterar_consulta(codigo, nova_data, nova_especialidade, novo_medico, novo_diagnostico):
    consulta = localizar_entidade(consultas, codigo)
    if consulta:
        if nova_data:
            consulta.data = nova_data
        if nova_especialidade:
            consulta.especialidade = nova_especialidade
        if novo_medico:
            consulta.medico = novo_medico
        if novo_diagnostico:
            consulta.diagnostico = novo_diagnostico
        salvar_todos_os_dados()
        st.success('Consulta atualizada com sucesso!')
    else:
        st.error('Consulta não encontrada.')

def cancelar_consulta(codigo):
    consulta = localizar_entidade(consultas, codigo)
    if consulta:
        consultas.remove(consulta)
        salvar_todos_os_dados()
        st.success('Consulta cancelada com sucesso!')
    else:
        st.error('Consulta não encontrada.')

def consultar_consulta(codigo):
    consulta = localizar_entidade(consultas, codigo)
    if consulta:
        st.write(f'Código: {consulta.codigo}')
        st.write(f'Código do Paciente: {consulta.codigo_paciente}')
        st.write(f'Data: {consulta.data}')
        st.write(f'Especialidade: {consulta.especialidade}')
        st.write(f'Médico: {consulta.medico}')
        st.write(f'Diagnóstico: {consulta.diagnostico}')
    else:
        st.error('Consulta não encontrada.')

def listar_consultas():
    if consultas:
        for consulta in consultas:
            st.text(str(consulta))
    else:
        st.write("Nenhuma consulta agendada.")

# Funções de manipulação de Prontuários
def adicionar_registro_prontuario(codigo_paciente, consulta_codigo):
    prontuario = localizar_prontuario(codigo_paciente)
    consulta = localizar_entidade(consultas, consulta_codigo)
    if prontuario and consulta:
        prontuario.adicionar_consulta(consulta)
        salvar_todos_os_dados()
        st.success('Registro adicionado ao prontuário com sucesso!')
    else:
        st.error("Prontuário ou consulta não encontrado.")

def consultar_prontuario(codigo_paciente):
    prontuario = localizar_prontuario(codigo_paciente)
    if prontuario:
        st.write(prontuario)
    else:
        st.error("Prontuário não encontrado.")

def listar_prontuarios():
    if prontuarios:
        for prontuario in prontuarios:
            st.text(str(prontuario))
    else:
        st.write("Nenhum prontuário disponível.")

# Streamlit
st.title('Sistema de Gerenciamento Hospitalar')

menu_opcao = st.sidebar.selectbox('Escolha uma opção', ['Gerenciar Pacientes', 'Gerenciar Consultas', 'Gerenciar Prontuários', 'Sair'])

if menu_opcao == 'Gerenciar Pacientes':
    st.subheader('Gerenciar Pacientes')
    opcao_paciente = st.sidebar.selectbox('Escolha uma ação', ['Cadastrar Paciente', 'Alterar Paciente', 'Excluir Paciente', 'Consultar Paciente', 'Listar Pacientes'])

    if opcao_paciente == 'Cadastrar Paciente':
        with st.form('Formulario_Paciente'):
            codigo = st.text_input('Código')
            nome = st.text_input('Nome completo')
            cpf = st.text_input('CPF')
            idade = st.text_input('Idade')
            genero = st.selectbox('Gênero', ['Masculino', 'Feminino', 'Outro'])
            submitted = st.form_submit_button('Cadastrar')
            if submitted:
                cadastrar_paciente(codigo, nome, cpf, idade, genero)

    elif opcao_paciente == 'Alterar Paciente':
        with st.form('Formulario_Alterar_Paciente'):
            codigo = st.text_input('Código do Paciente')
            nome = st.text_input('Novo nome (deixe em branco para manter)')
            cpf = st.text_input('Novo CPF (deixe em branco para manter)')
            idade = st.text_input('Nova idade (deixe em branco para manter)')
            genero = st.selectbox('Novo gênero (selecione para alterar)', ['Masculino', 'Feminino', 'Outro'], index=0)
            submitted = st.form_submit_button('Alterar')
            if submitted:
                alterar_paciente(codigo, nome, cpf, idade, genero)

    elif opcao_paciente == 'Excluir Paciente':
        codigo = st.text_input('Código do Paciente para excluir')
        if st.button('Excluir'):
            excluir_paciente(codigo)

    elif opcao_paciente == 'Consultar Paciente':
        codigo = st.text_input('Código do Paciente para consultar')
        if st.button('Consultar'):
            consultar_paciente(codigo)

    elif opcao_paciente == 'Listar Pacientes':
        listar_pacientes()

elif menu_opcao == 'Gerenciar Consultas':
    st.subheader('Gerenciar Consultas')
    opcao_consulta = st.sidebar.selectbox('Escolha uma ação', ['Agendar Consulta', 'Alterar Consulta', 'Cancelar Consulta', 'Consultar Consulta', 'Listar Consultas'])

    if opcao_consulta == 'Agendar Consulta':
        with st.form('Formulario_Consulta'):
            codigo_consulta = st.text_input('Código da consulta')
            codigo_paciente = st.text_input('Código do paciente')
            data_consulta = st.text_input('Data da consulta (DD-MM-AAAA)')
            especialidade = st.text_input('Especialidade')
            medico = st.text_input('Médico')
            diagnostico = st.text_area('Diagnóstico (opcional)')
            submitted = st.form_submit_button('Agendar')
            if submitted:
                agendar_consulta(codigo_consulta, codigo_paciente, data_consulta, especialidade, medico, diagnostico)

    elif opcao_consulta == 'Alterar Consulta':
        with st.form('Formulario_Alterar_Consulta'):
            codigo = st.text_input('Código da Consulta')
            nova_data = st.text_input('Nova data (DD-MM-AAAA)')
            nova_especialidade = st.text_input('Nova especialidade')
            novo_medico = st.text_input('Novo médico')
            novo_diagnostico = st.text_input('Novo diagnóstico (opcional)')
            submitted = st.form_submit_button('Alterar')
            if submitted:
                alterar_consulta(codigo, nova_data, nova_especialidade, novo_medico, novo_diagnostico)

    elif opcao_consulta == 'Cancelar Consulta':
        codigo = st.text_input('Código da Consulta para cancelar')
        if st.button('Cancelar'):
            cancelar_consulta(codigo)

    elif opcao_consulta == 'Consultar Consulta':
        codigo = st.text_input('Código da Consulta para consultar')
        if st.button('Consultar'):
            consultar_consulta(codigo)

    elif opcao_consulta == 'Listar Consultas':
        listar_consultas()

elif menu_opcao == 'Gerenciar Prontuários':
    st.subheader('Gerenciar Prontuários')
    opcao_prontuario = st.sidebar.selectbox('Escolha uma ação', ['Adicionar Registro ao Prontuário', 'Consultar Prontuário', 'Listar Prontuários'])

    if opcao_prontuario == 'Adicionar Registro ao Prontuário':
        with st.form('Formulario_Adicionar_Prontuario'):
            codigo_paciente = st.text_input('Código do paciente')
            consulta_codigo = st.text_input('Código da consulta')
            submitted = st.form_submit_button('Adicionar ao Prontuário')
            if submitted:
                adicionar_registro_prontuario(codigo_paciente, consulta_codigo)

    elif opcao_prontuario == 'Consultar Prontuário':
        codigo_paciente = st.text_input('Código do paciente para consultar prontuário')
        if st.button('Consultar'):
            consultar_prontuario(codigo_paciente)

    elif opcao_prontuario == 'Listar Prontuários':
        listar_prontuarios()

elif menu_opcao == 'Sair':
    st.stop()
