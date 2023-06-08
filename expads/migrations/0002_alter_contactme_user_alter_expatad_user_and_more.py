# Generated by Django 4.2.1 on 2023-06-07 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_user'),
        ('expads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='expatad',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='interested',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]
