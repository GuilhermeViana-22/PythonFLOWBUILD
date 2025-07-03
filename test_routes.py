#!/usr/bin/env python3
"""
Script para testar todas as rotas da nova estrutura do projeto
"""
import requests
import sys

BASE_URL = "http://127.0.0.1:8000"

# Rotas para testar
ROUTES = [
    "/dashboard/",
    "/users/",
    "/permissions/roles/",
    "/permissions/permissions/",
    "/positions/",
    "/flows/builder/",
    "/flows/templates/",
    "/flows/integrations/",
    "/history/",
    "/settings/general/",
    "/settings/security/",
    "/settings/notifications/",
    "/tasks/",
    "/profile/",
    "/configurations/",
    "/interpreter/",
]

def test_routes():
    """Testa todas as rotas da aplicação"""
    print("🧪 Testando rotas da nova estrutura...")
    print("=" * 50)
    
    results = []
    
    for route in ROUTES:
        url = f"{BASE_URL}{route}"
        try:
            response = requests.get(url, timeout=5)
            status = "✅ OK" if response.status_code in [200, 302] else f"❌ {response.status_code}"
            results.append((route, status, response.status_code))
            print(f"{route:<25} {status}")
        except requests.exceptions.RequestException as e:
            results.append((route, "❌ ERROR", str(e)))
            print(f"{route:<25} ❌ ERROR: {e}")
    
    print("\n" + "=" * 50)
    print("📊 Resumo dos testes:")
    
    success_count = sum(1 for _, status, _ in results if "✅" in status)
    total_count = len(results)
    
    print(f"✅ Sucessos: {success_count}/{total_count}")
    print(f"❌ Falhas: {total_count - success_count}/{total_count}")
    
    if success_count == total_count:
        print("\n🎉 Todos os testes passaram! A nova estrutura está funcionando.")
    else:
        print("\n⚠️  Algumas rotas falharam. Verifique a configuração.")
        
    return success_count == total_count

if __name__ == "__main__":
    print("🚀 Testador de Rotas - PythonFlowBuild")
    print("Certifique-se de que o servidor está rodando em http://127.0.0.1:8000")
    print()
    
    try:
        success = test_routes()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Teste interrompido pelo usuário.")
        sys.exit(1) 