# 🍞 Sistema de Breadcrumbs Automático

## 📋 Sobre o Sistema

O sistema de breadcrumbs foi implementado para fornecer navegação consistente e intuitiva em todas as páginas do PythonFlowBuild. O sistema detecta automaticamente a rota atual e gera os breadcrumbs correspondentes.

## 🎯 Funcionalidades

### ✅ Breadcrumbs Automáticos
- **Dashboard**: Sempre presente como home/início
- **System Config**: Aparece em todas as páginas de configuração
- **Detecção de Rota**: Identifica automaticamente a página atual
- **Ícones**: Cada breadcrumb tem um ícone específico
- **Links**: Breadcrumbs anteriores são clicáveis, página atual não

### ✅ Rotas Suportadas

#### 📊 Dashboard
- `/dashboard/` → Dashboard

#### 👥 Users
- `/users/` → Dashboard > Users
- `/users/{id}/` → Dashboard > Users > User Details
- `/users/{id}/delete/` → Dashboard > Users > Delete User

#### 🔐 Permissions
- `/permissions/roles/` → Dashboard > Roles
- `/permissions/roles/{id}/edit/` → Dashboard > Roles > Edit Role
- `/permissions/permissions/` → Dashboard > Permissions
- `/permissions/permissions/{id}/edit/` → Dashboard > Permissions > Edit Permission

#### 💼 Positions
- `/positions/` → Dashboard > Positions
- `/positions/{id}/edit/` → Dashboard > Positions > Edit Position

#### 🔄 Flows
- `/flows/builder/` → Dashboard > Flow Builder
- `/flows/templates/` → Dashboard > Flow Templates
- `/flows/integrations/` → Dashboard > Flow Integrations

#### ⚙️ Settings (System Config)
- `/settings/general/` → Dashboard > System Config > General Settings
- `/settings/security/` → Dashboard > System Config > Security Settings
- `/settings/notifications/` → Dashboard > System Config > Notifications
- `/configurations/` → Dashboard > System Config > System Configurations

#### 🔧 Outras Páginas
- `/interpreter/` → Dashboard > Interpreter
- `/history/` → Dashboard > History
- `/tasks/` → Dashboard > Tasks
- `/profile/` → Dashboard > Profile

## 🏗️ Implementação Técnica

### 1. Context Processor
**Arquivo**: `mvp_project/context_processors.py`
- Detecta automaticamente a URL atual
- Mapeia rotas para breadcrumbs
- Retorna estrutura de breadcrumbs e título da página atual

### 2. Template Base
**Arquivo**: `templates/dashboard/topbar.html`
- Renderiza breadcrumbs dinamicamente
- Exibe ícone e título da página atual
- Permite navegação através dos breadcrumbs

### 3. Configuração
**Arquivo**: `mvp_project/settings.py`
- Context processor registrado em `TEMPLATES`
- Disponível em todos os templates que estendem `base_dashboard.html`

## 🎨 Estrutura Visual

```
Dashboard > System Config > General Settings
   ↑           ↑              ↑
[clicável] [clicável]   [página atual]
```

### Características Visuais:
- **Links clicáveis**: Cor azul com hover
- **Página atual**: Cor cinza (não clicável)
- **Separadores**: Barras `/` entre breadcrumbs
- **Ícones**: Cada item tem um ícone específico
- **Responsivo**: Esconde em telas pequenas (mobile)

## 📝 Como Usar

### Para Desenvolvedores

1. **Adicionar Nova Rota**:
   ```python
   # Em mvp_project/context_processors.py
   breadcrumb_map = {
       '/nova-rota/': {'title': 'Nova Página', 'icon': 'fas fa-nova-icon'},
   }
   ```

2. **Template deve estender base_dashboard.html**:
   ```html
   {% extends 'dashboard/base_dashboard.html' %}
   {% block title %}Título da Página{% endblock %}
   {% block content %}
   <!-- Conteúdo da página -->
   {% endblock %}
   ```

3. **Variáveis disponíveis no template**:
   - `{{ breadcrumbs }}` - Lista de breadcrumbs
   - `{{ current_page_title }}` - Título da página atual

### Para Usuários

1. **Navegação**: Clique em qualquer breadcrumb para navegar
2. **Orientação**: Sempre saiba onde está na aplicação
3. **Volta rápida**: Clique em "Dashboard" para voltar ao início

## 🔧 Manutenção

### Adicionar Nova Categoria
Para adicionar uma nova categoria (como "System Config"):

1. **Identificar URL pattern**:
   ```python
   if url_path.startswith('/nova-categoria/'):
       breadcrumbs.append({
           'title': 'Nova Categoria',
           'url': None,
           'icon': 'fas fa-icon'
       })
   ```

2. **Mapear rotas específicas**:
   ```python
   '/nova-categoria/pagina/': {
       'title': 'Nome da Página', 
       'icon': 'fas fa-icon'
   },
   ```

### Detectar Subpáginas
Para páginas com IDs ou parâmetros:

```python
if '/categoria/' in url_path and '/edit/' in url_path:
    breadcrumbs.append({
        'title': 'Categoria',
        'url': '/categoria/',
        'icon': 'fas fa-icon'
    })
    breadcrumbs.append({
        'title': 'Editar Item',
        'url': None,
        'icon': 'fas fa-edit'
    })
```

## 🎯 Benefícios

1. **UX Consistente**: Navegação padronizada em todo o sistema
2. **Orientação**: Usuários sempre sabem onde estão
3. **Navegação Rápida**: Acesso direto a páginas anteriores
4. **Automático**: Breadcrumbs gerados automaticamente
5. **Responsivo**: Funciona em desktop e mobile
6. **Acessível**: Suporte a leitores de tela

## 📋 Exemplo de Uso

### Navegação Típica:
1. **Dashboard** → Página inicial
2. **Dashboard > Users** → Lista de usuários
3. **Dashboard > Users > User Details** → Detalhes do usuário
4. **Dashboard > System Config > General Settings** → Configurações gerais

### No Template:
```html
<!-- Os breadcrumbs aparecem automaticamente no topbar -->
<!-- Título da página é atualizado automaticamente -->
<!-- Ícone da página é atualizado automaticamente -->
```

---

**✅ Sistema implementado e funcionando!**

O sistema de breadcrumbs agora está ativo em todas as páginas que estendem `base_dashboard.html`. Navegue pelo sistema para ver os breadcrumbs em ação! 