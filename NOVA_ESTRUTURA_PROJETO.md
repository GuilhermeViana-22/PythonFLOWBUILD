# Nova Estrutura do Projeto - PythonFlowBuild

## Reorganização das Apps

O projeto foi reestruturado para uma melhor organização e manutenibilidade. A partir de agora, cada funcionalidade tem sua própria app:

### 📁 Apps Organizadas

#### 1. **Dashboard** (`dashboard/`)
- **Responsabilidade:** Interface principal do sistema
- **Rota:** `/dashboard/`
- **Funcionalidades:**
  - Tela principal do dashboard
  - Navegação central

#### 2. **Users** (`users/`)
- **Responsabilidade:** Gerenciamento de usuários
- **Rota:** `/users/`
- **Funcionalidades:**
  - Listagem de usuários
  - Detalhes do usuário
  - Exclusão de usuários
- **Modelos:** `DashboardUser`

#### 3. **Permissions** (`permissions/`)
- **Responsabilidade:** Gerenciamento de permissões e roles
- **Rota:** `/permissions/`
- **Funcionalidades:**
  - Gerenciamento de roles
  - Gerenciamento de permissões
  - Edição de roles e permissões
- **Modelos:** `Role`, `CustomPermission`

#### 4. **Positions** (`positions/`)
- **Responsabilidade:** Gerenciamento de cargos/posições
- **Rota:** `/positions/`
- **Funcionalidades:**
  - Listagem de posições
  - Edição de posições
- **Modelos:** `Position`

#### 5. **Flows** (`flows/`)
- **Responsabilidade:** Construtor de fluxos
- **Rota:** `/flows/`
- **Funcionalidades:**
  - Flow Builder
  - Templates de fluxo
  - Integrações de fluxo

#### 6. **History** (`history/`)
- **Responsabilidade:** Histórico e comparação de arquivos
- **Rota:** `/history/`
- **Funcionalidades:**
  - Comparação de arquivos JSON
  - Visualização de diferenças

#### 7. **Settings** (`settings/`)
- **Responsabilidade:** Configurações do sistema
- **Rota:** `/settings/`
- **Funcionalidades:**
  - Configurações gerais
  - Configurações de segurança
  - Configurações de notificações

#### 8. **Tasks** (`tasks/`)
- **Responsabilidade:** Gerenciamento de tarefas
- **Rota:** `/tasks/`
- **Funcionalidades:**
  - Listagem de tarefas
  - Gerenciamento de tarefas

#### 9. **User Profile** (`user_profile/`)
- **Responsabilidade:** Perfil do usuário
- **Rota:** `/profile/`
- **Funcionalidades:**
  - Visualização do perfil
  - Edição do perfil

#### 10. **Configurations** (`configurations/`)
- **Responsabilidade:** Configurações avançadas
- **Rota:** `/configurations/`
- **Funcionalidades:**
  - Configurações do sistema

#### 11. **Interpreter** (`interpreter/`)
- **Responsabilidade:** Interpretador de código
- **Rota:** `/interpreter/`
- **Funcionalidades:**
  - Interface do interpretador

### 📄 Templates Organizados

Cada app agora tem sua própria pasta de templates:

```
templates/
├── dashboard/
│   ├── dashboard.html
│   ├── base_dashboard.html
│   ├── sidebar.html
│   ├── topbar.html
│   └── footer.html
├── users/
│   ├── users_all.html
│   ├── user_detail.html
│   └── user_confirm_delete.html
├── permissions/
│   ├── users_roles.html
│   ├── role_edit.html
│   ├── users_permissions.html
│   └── permission_edit.html
├── positions/
│   ├── positions.html
│   └── position_edit.html
├── flows/
│   ├── flow_builder.html
│   ├── flow_templates.html
│   └── flow_integrations.html
├── history/
│   └── history.html
├── settings/
│   ├── settings_general.html
│   ├── settings_security.html
│   └── settings_notifications.html
├── tasks/
│   └── tasks.html
├── user_profile/
│   └── profile.html
├── configurations/
│   └── configurations.html
└── interpreter/
    └── interpreter.html
```

### 🚀 Benefícios da Nova Estrutura

1. **Organização:** Cada funcionalidade tem sua própria app
2. **Manutenibilidade:** Código mais fácil de manter e debugar
3. **Escalabilidade:** Mais fácil adicionar novas funcionalidades
4. **Responsabilidade única:** Cada app tem uma responsabilidade específica
5. **Reutilização:** Código mais reutilizável e modular

### 🔧 Como Usar

1. **Executar migrações:** `python3 manage.py migrate`
2. **Criar superusuário:** `python3 manage.py createsuperuser`
3. **Iniciar servidor:** `python3 manage.py runserver`

### 📋 Próximos Passos

1. Atualizar links no sidebar para usar as novas rotas
2. Testar todas as funcionalidades
3. Implementar testes unitários para cada app
4. Documentar APIs se necessário
5. Configurar permissões específicas para cada app

### 🌐 Rotas Principais

- Dashboard: `/dashboard/`
- Usuários: `/users/`
- Permissões: `/permissions/`
- Posições: `/positions/`
- Fluxos: `/flows/`
- Histórico: `/history/`
- Configurações: `/settings/`
- Tarefas: `/tasks/`
- Perfil: `/profile/`
- Configurações Avançadas: `/configurations/`
- Interpretador: `/interpreter/`

Esta nova estrutura torna o projeto mais profissional e facilita o desenvolvimento futuro! 