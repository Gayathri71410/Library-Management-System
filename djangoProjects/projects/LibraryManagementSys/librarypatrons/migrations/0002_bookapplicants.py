# Generated by Django 5.0.1 on 2024-02-02 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_rename_easysearch_bookdetails_published_year_and_more'),
        ('librarypatrons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookApplicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('id_document', models.FileField(upload_to='id_document')),
                ('department', models.TextField()),
                ('book_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.bookdetails')),
            ],
        ),
    ]