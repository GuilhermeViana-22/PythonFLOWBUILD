# MVP Project Django

Um projeto MVP (Minimum Viable Product) construído com Django e Bootstrap.

## Funcionalidades

- ✅ Página Welcome com design responsivo
- ✅ Interface moderna usando Bootstrap 5
- ✅ Navegação intuitiva
- ✅ Seções organizadas (Hero, Features, Call to Action)
- ✅ Design mobile-first

## Instalação

1. Clone o repositório
2. Crie e ative um ambiente virtual e instale as dependências executando o
   script `setup.sh`:
   ```bash
   ./setup.sh
   ```

3. Execute as migrações:
   ```bash
   python3 manage.py migrate
   ```

4. Inicie o servidor:
   ```bash
   python3 manage.py runserver
   ```

5. Acesse o projeto em: `http://localhost:8000`

### Configuração do MySQL

O projeto utiliza MySQL por padrão. Defina as variáveis de ambiente abaixo ou
edite `mvp_project/settings.py` conforme necessário:

```bash
export MYSQL_DB=mvp_db
export MYSQL_USER=root
export MYSQL_PASSWORD=senha
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
```

## Estrutura do Projeto

```
PythonFlowBuild/
├── mvp_project/          # Configurações do projeto
│   ├── settings.py       # Configurações do Django
│   ├── urls.py          # URLs principais
│   └── wsgi.py          # WSGI configuration
├── welcome/             # App principal
│   ├── views.py         # Views do app
│   ├── urls.py          # URLs do app
│   └── templates/       # Templates HTML
└── manage.py           # Script de gerenciamento do Django
```

## Tecnologias Utilizadas

- **Django 4.2.23**: Framework web Python
- **Bootstrap 5.3.0**: Framework CSS responsivo
- **MySQL**: Banco de dados utilizado
- **HTML5/CSS3**: Estrutura e estilo

## Próximos Passos

Para expandir este MVP, você pode:

1. Adicionar autenticação de usuários
2. Implementar um sistema de contato
3. Adicionar páginas "Sobre" e "Contato"
4. Integrar com APIs externas
5. Implementar testes automatizados
6. Configurar deployment para produção

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. 