#!/bin/bash

# Script para iniciar o projeto Django
echo "🚀 Iniciando o projeto Python Flow Build..."

# Ativar o ambiente virtual
echo "📦 Ativando ambiente virtual..."
source venv/bin/activate

# Aplicar migrações (se necessário)
echo "🔧 Aplicando migrações..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Iniciar o servidor
echo "🌐 Iniciando servidor Django..."
echo "Acesse: http://localhost:8000/"
echo ""
echo "👥 Usuários disponíveis:"
echo "  - Admin: admin / admin123"
echo "  - Usuário: user@test.com / senha123"
echo "  - Usuário: testuser / senha123"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo "----------------------------------------"

python manage.py runserver 