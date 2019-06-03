# Generated by Django 2.0.2 on 2019-06-02 22:05

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_api', '0014_auto_20190602_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile_employer', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employer_name', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=60)),
                ('office_number', models.IntegerField(blank=True, default=0)),
                ('commercial_category', models.IntegerField(default=0)),
                ('specialty_demand', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[0], size=None)),
                ('hiring_number', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='formation',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='schedule',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]