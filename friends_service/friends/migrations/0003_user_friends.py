# Generated by Django 4.2.2 on 2023-06-09 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("friends", "0002_friendrequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="friends",
            field=models.ManyToManyField(blank=True, to="friends.user"),
        ),
    ]
