# Generated by Django 5.0.1 on 2024-01-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookTitle', models.CharField(max_length=300)),
                ('BookId', models.CharField(max_length=300)),
                ('BookYear', models.CharField(choices=[('1styear', '1st yr'), ('2ndyear', '2nd yr')], max_length=20)),
                ('benefits', models.TextField()),
                ('easysearch', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Managebooksdetails',
        ),
    ]
