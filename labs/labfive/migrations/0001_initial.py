# Generated by Django 4.2 on 2023-05-07 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('manufacturing_since', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('launch_date', models.DateField()),
                ('platform', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labfive.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labfive.model')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labfive.review')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='model',
            field=models.ManyToManyField(through='labfive.ReviewModel', to='labfive.model'),
        ),
    ]
