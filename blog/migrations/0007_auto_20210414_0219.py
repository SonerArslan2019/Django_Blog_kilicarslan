# Generated by Django 3.1.7 on 2021-04-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_iletisimmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yorummodel',
            name='guncellenme_tarihi',
        ),
        migrations.AddField(
            model_name='yorummodel',
            name='duzenlenme_tarihi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
