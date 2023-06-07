# Generated by Django 4.2.1 on 2023-06-04 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bbgproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('locationcode', models.CharField(max_length=200)),
                ('sublocationcode', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Description', models.CharField(max_length=500)),
                ('contactno', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('is_active', models.BooleanField(default=True)),
                ('cover_photo', models.FileField(blank=True, null=True, upload_to='users/bbgcover_photos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expads.category')),
                ('citycode', models.ForeignKey(default='Jeddah', on_delete=django.db.models.deletion.CASCADE, to='expads.citycode')),
                ('countrycode', models.ForeignKey(default='Saudi Arabia', on_delete=django.db.models.deletion.CASCADE, to='expads.countrycode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'bbgproject',
                'verbose_name_plural': 'bbgprojects',
                'ordering': ('-created', '-updated'),
            },
        ),
        migrations.CreateModel(
            name='BbgImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, null=True, upload_to='users/bbgimages')),
                ('bbgprojects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bbgproject', to='bbg.bbgproject')),
            ],
        ),
    ]
