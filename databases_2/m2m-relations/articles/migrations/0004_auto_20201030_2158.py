# Generated by Django 3.1.2 on 2020-10-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20201028_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scopes',
            old_name='article_scope',
            new_name='scope',
        ),
        migrations.RemoveField(
            model_name='scopes',
            name='members',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='article',
        ),
        migrations.AddField(
            model_name='membership',
            name='article',
            field=models.ManyToManyField(to='articles.Article'),
        ),
    ]
