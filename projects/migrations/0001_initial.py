# Generated by Django 3.1.7 on 2021-03-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='project_<built-in function id>/')),
                ('text', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('categorie', models.CharField(choices=[('BG', 'BLOG'), ('EN', 'ENTERTAINMENT'), ('EC', 'ECOMMERCE'), ('TC', 'TECH'), ('O', 'OTHER')], max_length=2)),
                ('link', models.URLField(verbose_name='link_to_project')),
                ('like', models.ManyToManyField(related_name='like', to='portfolio.UserProfile')),
                ('tools', models.ManyToManyField(related_name='tools', to='tags.Tag')),
                ('user', models.ManyToManyField(related_name='project_user', to='portfolio.UserProfile')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]