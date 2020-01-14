# Generated by Django 2.1.5 on 2020-01-14 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20181028_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('length', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='Box',
            name='author',
        ),
        migrations.RemoveField(
            model_name='Box',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='Box',
            name='language',
        ),
       
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.RenameField(
            model_name='author',
         
            new_name='name',
        ),
        
        migrations.DeleteModel(
            name='Box',
        ),
        
       
        migrations.AddField(
            model_name='box',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author'),
        ),
    ]
