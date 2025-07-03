from django.db import migrations
from django.utils import timezone


def create_users(apps, schema_editor):
    User = apps.get_model('dashboard', 'DashboardUser')
    sample_data = [
        {
            'name': f'User {i}',
            'cpf': f'0000000000{i:04d}',
            'email': f'user{i}@example.com',
            'password': 'pbkdf2sha256$dummy',
            'telefone_celular': f'+123456789{i:02d}',
        } for i in range(1, 11)
    ]
    for data in sample_data:
        User.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
