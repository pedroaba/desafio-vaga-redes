# Generated by Django 4.1.4 on 2022-12-28 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networking', '0002_alter_city_options_alter_networking_enodeb_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkinginformation',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]