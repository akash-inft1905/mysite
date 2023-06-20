# Generated by Django 4.1.2 on 2023-06-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_image', models.CharField(blank=True, max_length=100, null=True, verbose_name='Google Drive Image Id')),
                ('service_name', models.CharField(blank=True, max_length=40, null=True)),
                ('shadow_icon', models.CharField(blank=True, max_length=40, null=True)),
                ('service_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Experience Section',
            },
        ),
    ]
