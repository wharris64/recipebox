# Generated by Django 2.2.7 on 2019-11-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0002_auto_20191120_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(related_name='fave', to='recipebox.Recipe'),
        ),
    ]
