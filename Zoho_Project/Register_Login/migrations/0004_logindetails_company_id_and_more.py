# Generated by Django 4.2 on 2023-12-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0003_alter_logindetails_distributor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindetails',
            name='company_id',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='logindetails',
            name='self_distributor',
            field=models.CharField(blank=True, default='self', max_length=100, null=True),
        ),
    ]
