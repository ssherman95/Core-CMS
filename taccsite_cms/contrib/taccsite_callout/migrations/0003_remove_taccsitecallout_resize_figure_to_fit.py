# Generated by Django 2.2.16 on 2021-12-15 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taccsite_callout', '0002_auto_20210928_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taccsitecallout',
            name='resize_figure_to_fit',
        ),
    ]