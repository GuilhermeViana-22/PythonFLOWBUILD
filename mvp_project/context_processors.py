from django.urls import resolve
from django.conf import settings

def breadcrumbs(request):
    """
    Context processor que gera breadcrumbs automaticamente baseado na URL atual
    """
    breadcrumbs = []
    
    # Sempre adiciona Dashboard como home
    breadcrumbs.append({
        'title': 'Dashboard',
        'url': '/dashboard/',
        'icon': 'fas fa-home'
    })
    
    # Mapeamento de rotas para breadcrumbs
    url_path = request.path
    
    # Configurações do sistema
    if url_path.startswith('/settings/') or url_path.startswith('/configurations/'):
        breadcrumbs.append({
            'title': 'System Config',
            'url': None,
            'icon': 'fas fa-cog'
        })
    
    # Mapeamento específico de rotas
    breadcrumb_map = {
        # Users
        '/users/': {'title': 'Users', 'icon': 'fas fa-users'},
        '/permissions/': {'title': 'Permissions', 'icon': 'fas fa-key'},
        '/permissions/roles/': {'title': 'Roles', 'icon': 'fas fa-user-tag'},
        '/permissions/permissions/': {'title': 'Permissions', 'icon': 'fas fa-key'},
        '/positions/': {'title': 'Positions', 'icon': 'fas fa-user-friends'},
        
        # Flows
        '/flows/': {'title': 'Flows', 'icon': 'fas fa-project-diagram'},
        '/flows/builder/': {'title': 'Flow Builder', 'icon': 'fas fa-tools'},
        '/flows/templates/': {'title': 'Flow Templates', 'icon': 'fas fa-copy'},
        '/flows/integrations/': {'title': 'Flow Integrations', 'icon': 'fas fa-plug'},
        
        # Other sections
        '/interpreter/': {'title': 'Interpreter', 'icon': 'fas fa-code'},
        '/history/': {'title': 'History', 'icon': 'fas fa-history'},
        '/tasks/': {'title': 'Tasks', 'icon': 'fas fa-tasks'},
        '/profile/': {'title': 'Profile', 'icon': 'fas fa-user'},
        
        # Settings
        '/settings/general/': {'title': 'General Settings', 'icon': 'fas fa-sliders-h'},
        '/settings/security/': {'title': 'Security Settings', 'icon': 'fas fa-shield-alt'},
        '/settings/notifications/': {'title': 'Notifications', 'icon': 'fas fa-bell'},
        '/configurations/': {'title': 'System Configurations', 'icon': 'fas fa-cogs'},
    }
    
    # Adiciona breadcrumb específico da rota atual
    if url_path in breadcrumb_map:
        breadcrumb_info = breadcrumb_map[url_path]
        breadcrumbs.append({
            'title': breadcrumb_info['title'],
            'url': None,  # Página atual não tem link
            'icon': breadcrumb_info['icon']
        })
    elif url_path == '/dashboard/':
        # Dashboard principal não adiciona breadcrumb extra
        pass
    
    # Detecta detalhes específicos (ex: edição de usuário)
    if '/users/' in url_path and url_path != '/users/':
        if url_path.endswith('/delete/'):
            breadcrumbs.append({
                'title': 'Users',
                'url': '/users/',
                'icon': 'fas fa-users'
            })
            breadcrumbs.append({
                'title': 'Delete User',
                'url': None,
                'icon': 'fas fa-trash'
            })
        elif url_path.count('/') == 2:  # /users/{id}/
            breadcrumbs.append({
                'title': 'Users',
                'url': '/users/',
                'icon': 'fas fa-users'
            })
            breadcrumbs.append({
                'title': 'User Details',
                'url': None,
                'icon': 'fas fa-user'
            })
    
    # Detecta edição de roles/permissions
    if '/permissions/' in url_path and '/edit/' in url_path:
        if 'roles' in url_path:
            breadcrumbs.append({
                'title': 'Roles',
                'url': '/permissions/roles/',
                'icon': 'fas fa-user-tag'
            })
            breadcrumbs.append({
                'title': 'Edit Role',
                'url': None,
                'icon': 'fas fa-edit'
            })
        elif 'permissions' in url_path:
            breadcrumbs.append({
                'title': 'Permissions',
                'url': '/permissions/permissions/',
                'icon': 'fas fa-key'
            })
            breadcrumbs.append({
                'title': 'Edit Permission',
                'url': None,
                'icon': 'fas fa-edit'
            })
    
    # Detecta edição de posições
    if '/positions/' in url_path and '/edit/' in url_path:
        breadcrumbs.append({
            'title': 'Positions',
            'url': '/positions/',
            'icon': 'fas fa-user-friends'
        })
        breadcrumbs.append({
            'title': 'Edit Position',
            'url': None,
            'icon': 'fas fa-edit'
        })
    
    return {
        'breadcrumbs': breadcrumbs,
        'current_page_title': breadcrumbs[-1]['title'] if breadcrumbs else 'Dashboard'
    } 