# Generated by Django 4.2.5 on 2023-09-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Ism kiriting: ')),
                ('comment', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.ImageField(default='projects/default.png', upload_to='projects/post_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('github', models.URLField(max_length=150)),
                ('domain', models.URLField(max_length=50)),
            ],
        ),
    ]
