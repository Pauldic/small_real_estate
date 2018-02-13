# Generated by Django 2.0.2 on 2018-02-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='core.Category', verbose_name='categories'),
        ),
    ]
