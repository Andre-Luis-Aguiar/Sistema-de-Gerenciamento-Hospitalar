# Sistema de Gerenciamento Hospitalar

## Descrição do Sistema

Este sistema foi desenvolvido para gerenciar informações relacionadas a pacientes, consultas e prontuários de um hospital. Ele permite o cadastro, alteração, exclusão e consulta de dados de pacientes, bem como o agendamento, alteração e cancelamento de consultas. Além disso, o sistema gerencia os prontuários dos pacientes, permitindo a adição de registros de consultas.

## Entidades

### Paciente
Representa um paciente do sistema. Contém os seguintes atributos:
- `codigo`: Código único do paciente.
- `nome`: Nome completo do paciente.
- `cpf`: CPF do paciente.
- `idade`: Idade do paciente.
- `genero`: Gênero do paciente.

### Consulta
Representa uma consulta médica. Contém os seguintes atributos:
- `codigo`: Código único da consulta.
- `codigo_paciente`: Código do paciente associado à consulta.
- `data`: Data da consulta.
- `especialidade`: Especialidade médica da consulta.
- `medico`: Nome do médico responsável pela consulta.
- `diagnostico`: Diagnóstico preliminar da consulta (opcional).

### Prontuario
Representa o prontuário de um paciente, contendo o histórico de consultas. Contém os seguintes atributos:
- `paciente`: Objeto da classe `Paciente` associado ao prontuário.
- `consultas`: Lista de objetos da classe `Consulta` associadas ao prontuário.

## Funcionalidades

### Gerenciamento de Pacientes
1. **Cadastrar Paciente**: Permite o cadastro de um novo paciente.
2. **Alterar Paciente**: Permite a alteração dos dados de um paciente existente.
3. **Excluir Paciente**: Permite a exclusão de um paciente e seus registros associados.
4. **Consultar Paciente**: Permite a consulta dos dados de um paciente.
5. **Listar Pacientes**: Exibe a lista de todos os pacientes cadastrados.

### Gerenciamento de Consultas
1. **Agendar Consulta**: Permite o agendamento de uma nova consulta para um paciente.
2. **Alterar Consulta**: Permite a alteração dos dados de uma consulta existente.
3. **Cancelar Consulta**: Permite o cancelamento de uma consulta.
4. **Consultar Consulta**: Permite a consulta dos dados de uma consulta.
5. **Listar Consultas**: Exibe a lista de todas as consultas agendadas.

### Gerenciamento de Prontuários
1. **Adicionar Registro ao Prontuário**: Permite adicionar uma consulta ao prontuário de um paciente.
2. **Consultar Prontuário**: Permite a consulta do prontuário de um paciente.
3. **Listar Prontuários**: Exibe a lista de todos os prontuários cadastrados.