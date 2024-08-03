# Generated by Django 5.0.7 on 2024-08-01 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0008_youtube_is_recent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogapp.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.CharField(choices=[('Programming', 'Programming'), ('Networking', 'Networking'), ('Trending', 'Trending'), ('Inspiration', 'Inspiration'), ('Latest Posts', 'Latest Posts')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogapp.post'),
        ),
    ]
