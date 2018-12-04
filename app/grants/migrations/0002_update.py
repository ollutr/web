# Generated by Django 2.1.2 on 2018-11-29 19:51

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('title', models.CharField(default='', help_text='The title of the Grant.', max_length=255)),
                ('description', models.TextField(blank=True, default='', help_text='The description of the Grant.')),
                ('grant', models.ForeignKey(help_text='The associated Grant.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='grants.Grant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
