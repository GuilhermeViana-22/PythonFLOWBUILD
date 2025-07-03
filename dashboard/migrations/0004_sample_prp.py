from django.db import migrations


def create_sample(apps, schema_editor):
    Position = apps.get_model('dashboard', 'Position')
    Role = apps.get_model('dashboard', 'Role')
    CustomPermission = apps.get_model('dashboard', 'CustomPermission')

    for i in range(1, 6):
        Position.objects.create(name=f'Position {i}', description='Sample position')
    for i in range(1, 6):
        Role.objects.create(name=f'Role {i}', description='Sample role')
    for i in range(1, 6):
        CustomPermission.objects.create(name=f'Permission {i}', code=f'perm_{i}', description='Sample permission')


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_positions_roles_permissions'),
    ]

    operations = [
        migrations.RunPython(create_sample),
    ]
