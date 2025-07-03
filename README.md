# PythonFlowBuild - Sistema MVC para Análise de Datasets em Plantas de Arquitetura

Um projeto Django seguindo padrão MVC (Model-View-Controller) especializado na leitura, processamento e análise de datasets relacionados a plantas de arquitetura.

## 🏗️ Sobre o Projeto

O PythonFlowBuild é um sistema web desenvolvido para arquitetos, engenheiros e profissionais da construção civil que precisam analisar e processar datasets de plantas arquitetônicas. O sistema oferece uma interface intuitiva para upload, visualização e análise de dados estruturais e arquitetônicos.

## 🎯 Funcionalidades

- ✅ Sistema de autenticação de usuários
- ✅ Interface responsiva com Bootstrap 5
- ✅ Upload e processamento de datasets arquitetônicos
- ✅ Análise e visualização de dados de plantas
- ✅ Painel administrativo para gerenciamento
- ✅ API RESTful para integração com outras ferramentas
- ✅ Sistema de perfis de usuário personalizado

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.8+
- pip3
- Ambiente virtual (recomendado)

### Instalação Rápida

1. Clone o repositório:
   ```bash
   git clone <repository-url>
   cd PythonFlowBuild
   ```

2. Use o script de inicialização:
   ```bash
   ./start_project.sh
   ```

### Instalação Manual

1. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

5. Acesse o projeto em: `http://localhost:8000`

## 👥 Usuários para Teste

- **Admin**: `admin` / `admin123`
- **Usuário**: `user@test.com` / `senha123`
- **Usuário**: `testuser` / `senha123`

## 🏗️ Arquitetura MVC

O projeto segue o padrão MVC (Model-View-Controller) implementado através do framework Django:

### Models (Modelos)
- `accounts/models.py`: Perfis de usuário
- `authentication/models.py`: Modelos de autenticação avançada
- Futuros modelos para datasets arquitetônicos

### Views (Controladores)
- `accounts/views.py`: Lógica de autenticação e perfis
- `welcome/views.py`: Página inicial e navegação
- `authentication/views.py`: API de autenticação

### Templates (Visões)
- `templates/base.html`: Template base responsivo
- `accounts/templates/`: Templates de autenticação
- `welcome/templates/`: Templates de boas-vindas

## 📂 Estrutura do Projeto

```
PythonFlowBuild/
├── accounts/                    # App de autenticação
│   ├── models.py               # Modelos de usuário
│   ├── views.py                # Views de autenticação
│   ├── forms.py                # Formulários de login/cadastro
│   └── templates/              # Templates de auth
├── welcome/                     # App principal
│   ├── views.py                # Views da página inicial
│   └── templates/              # Templates de boas-vindas
├── authentication/              # App de API
│   ├── models.py               # Modelos de API
│   └── views.py                # Views da API
├── mvp_project/                # Configurações Django
│   ├── settings.py             # Configurações do projeto
│   ├── urls.py                 # URLs principais
│   └── wsgi.py                 # Configuração WSGI
├── templates/                   # Templates globais
│   └── base.html               # Template base
├── requirements.txt            # Dependências Python
├── start_project.sh           # Script de inicialização
└── manage.py                  # Script de gerenciamento Django
```

## 🛠️ Tecnologias Utilizadas

- **Django 4.2.23**: Framework web Python seguindo padrão MVC
- **Django REST Framework**: Para desenvolvimento de APIs
- **Bootstrap 5.3.0**: Framework CSS responsivo
- **SQLite**: Banco de dados para desenvolvimento
- **JWT**: Autenticação segura via tokens
- **HTML5/CSS3**: Frontend responsivo

## 🔜 Próximos Passos

Para expandir o sistema de análise de datasets arquitetônicos:

1. **Módulo de Upload**: Implementar upload de arquivos CAD/DWG
2. **Processamento de Dados**: Análise automática de plantas
3. **Visualização 3D**: Renderização de modelos arquitetônicos
4. **Relatórios**: Geração de relatórios técnicos
5. **Integração BIM**: Compatibilidade com software BIM
6. **Machine Learning**: Análise inteligente de padrões arquitetônicos
7. **API Avançada**: Endpoints para integração com CAD software

## 🎨 Casos de Uso

- **Arquitetos**: Análise de eficiência espacial em plantas
- **Engenheiros**: Validação de estruturas e dimensionamentos
- **Construtoras**: Otimização de projetos e custos
- **Urbanistas**: Análise de densidade e aproveitamento
- **Acadêmicos**: Pesquisa em padrões arquitetônicos

## 📊 Datasets Suportados

- Plantas baixas em formato CAD
- Dados de dimensionamento estrutural
- Informações de materiais e acabamentos
- Dados de eficiência energética
- Análises de iluminação e ventilação

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📧 Contato

Para dúvidas sobre o sistema de análise de datasets arquitetônicos, entre em contato através do sistema de issues do GitHub. 