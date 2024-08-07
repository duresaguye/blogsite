# Generated by Django 5.0 on 2024-03-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0006_youtube_delete_podcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube',
            name='status',
            field=models.CharField(choices=[('0', 'Draft'), ('1', 'Published')], default=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='youtube',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
