# Generated by Django 2.2.7 on 2019-11-09 16:34

from django.db import migrations, models
import internship_finder.companies.models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_remove_office_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=internship_finder.companies.models.get_logo_path),
        ),
    ]
