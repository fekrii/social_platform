# Generated by Django 4.1.1 on 2022-09-27 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='EventPost',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.basepost')),
                ('eventName', models.CharField(blank=True, max_length=255, null=True)),
                ('eventStartTime', models.DateTimeField()),
                ('eventLocation', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('post.basepost',),
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.basepost')),
                ('content', models.TextField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('post.basepost',),
        ),
        migrations.CreateModel(
            name='TravelPost',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.basepost')),
                ('content', models.TextField(blank=True, max_length=255, null=True)),
                ('destinationCountry', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('post.basepost',),
        ),
    ]
