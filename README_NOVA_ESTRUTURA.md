# 🚀 PythonFlowBuild - Nova Estrutura Organizada

## 📝 Sobre o Projeto

Este projeto foi completamente reorganizado para uma estrutura mais profissional e modular. Cada funcionalidade agora está em sua própria app Django, facilitando a manutenção e desenvolvimento.

## 🏗️ Estrutura do Projeto

### 📂 Apps Principais

```
PythonFlowBuild/
├── 🏠 dashboard/          # Interface principal
├── 👥 users/              # Gerenciamento de usuários
├── 🔐 permissions/        # Roles e permissões
├── 💼 positions/          # Cargos e posições
├── 🔄 flows/              # Construtor de fluxos
├── 📊 history/            # Histórico e comparações
├── ⚙️ settings/           # Configurações do sistema
├── ✅ tasks/              # Gerenciamento de tarefas
├── 👤 user_profile/       # Perfil do usuário
├── 🔧 configurations/     # Configurações avançadas
├── 🖥️ interpreter/        # Interpretador de código
├── 🔑 accounts/           # Autenticação básica
├── 🛡️ authentication/     # Autenticação JWT
└── 👋 welcome/            # Página inicial
```

### 🌐 Rotas Organizadas

| App | Rota | Funcionalidade |
|-----|------|----------------|
| Dashboard | `/dashboard/` | Interface principal |
| Users | `/users/` | Gerenciamento de usuários |
| Permissions | `/permissions/` | Roles e permissões |
| Positions | `/positions/` | Cargos e posições |
| Flows | `/flows/` | Construtor de fluxos |
| History | `/history/` | Histórico e comparações |
| Settings | `/settings/` | Configurações |
| Tasks | `/tasks/` | Tarefas |
| Profile | `/profile/` | Perfil do usuário |
| Configurations | `/configurations/` | Configurações avançadas |
| Interpreter | `/interpreter/` | Interpretador |

## 🚀 Como Executar

### 1. Preparar o Ambiente

```bash
# Ativar o ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar o Banco de Dados

```bash
# Executar migrações
python3 manage.py migrate

# Criar superusuário
python3 manage.py createsuperuser
```

### 3. Iniciar o Servidor

```bash
# Executar servidor
python3 manage.py runserver
```

### 4. Testar as Rotas

```bash
# Executar o script de teste
python3 test_routes.py
```

## 📋 Funcionalidades por App

### 🏠 Dashboard
- Tela principal do sistema
- Navegação centralizada
- Visão geral das funcionalidades

### 👥 Users
- Listagem de usuários
- Detalhes do usuário
- Exclusão de usuários
- Busca por usuários

### 🔐 Permissions
- Gerenciamento de roles
- Gerenciamento de permissões
- Edição de roles e permissões
- Associação de permissões

### 💼 Positions
- Listagem de posições/cargos
- Edição de posições
- Criação de novas posições

### 🔄 Flows
- Flow Builder (construtor visual)
- Templates de fluxo
- Integrações de fluxo
- Gerenciamento de workflows

### 📊 History
- Comparação de arquivos JSON
- Visualização de diferenças
- Histórico de alterações

### ⚙️ Settings
- Configurações gerais
- Configurações de segurança
- Configurações de notificações

### ✅ Tasks
- Gerenciamento de tarefas
- Status de tarefas
- Atribuição de tarefas

### 👤 User Profile
- Visualização do perfil
- Edição de dados pessoais
- Configurações do usuário

### 🔧 Configurations
- Configurações avançadas do sistema
- Parâmetros de configuração

### 🖥️ Interpreter
- Interface do interpretador
- Execução de código
- Ambiente de desenvolvimento

## 🎯 Benefícios da Nova Estrutura

1. **🔧 Modularidade**: Cada funcionalidade isolada
2. **🚀 Escalabilidade**: Fácil adição de novas features
3. **🛠️ Manutenibilidade**: Código mais fácil de manter
4. **🧪 Testabilidade**: Testes mais específicos
5. **👥 Colaboração**: Trabalho em equipe mais organizado

## 📚 Documentação

- [Nova Estrutura](NOVA_ESTRUTURA_PROJETO.md) - Documentação detalhada
- [Instruções de Setup](SETUP_INSTRUCTIONS.md) - Configuração inicial
- [Projeto Funcionando](PROJETO_FUNCIONANDO.md) - Status do projeto

## 🔄 Próximos Passos

1. ✅ Estrutura reorganizada
2. ✅ Apps criadas e configuradas
3. ✅ Templates organizados
4. ✅ Migrações executadas
5. 🔲 Atualizar sidebar com novas rotas
6. 🔲 Implementar testes unitários
7. 🔲 Configurar permissões específicas
8. 🔲 Documentar APIs

## 🤝 Contribuindo

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Faça commit das suas alterações
4. Faça push para a branch
5. Abra um Pull Request

## 📧 Contato

Para dúvidas sobre a nova estrutura, consulte a documentação ou entre em contato.

---

✨ **Agora o projeto está mais organizado e profissional!** ✨ 