# Generated by Django 5.0.1 on 2024-01-31 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_bookdetails_delete_managebooksdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookdetails',
            old_name='easysearch',
            new_name='published_year',
        ),
        migrations.RenameField(
            model_name='bookdetails',
            old_name='benefits',
            new_name='remarks',
        ),
    ]