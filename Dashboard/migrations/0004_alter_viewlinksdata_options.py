# Generated by Django 4.0.1 on 2022-01-17 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_alter_viewlinksdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewlinksdata',
            options={'ordering': ['-id']},
        ),
    ]