# Generated by Django 5.2 on 2025-06-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0015_alter_post_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]
