# Generated by Django 5.1.6 on 2025-02-09 02:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("slack", "0002_alter_event_channel_id_alter_event_channel_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="command",
        ),
    ]
