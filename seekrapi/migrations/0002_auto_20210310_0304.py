# Generated by Django 3.1.7 on 2021-03-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekrapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='company_logo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='profile_img',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='seekerprofile',
            name='profile_img',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='seekerprofile',
            name='project_img',
            field=models.TextField(),
        ),
    ]
