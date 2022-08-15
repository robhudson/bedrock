# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 3.2.12 on 2022-03-25 18:43

from django.core import management
from django.db import migrations, models


def clear_positions(apps, schema_editor):
    Position = apps.get_model("careers", "Position")
    Position.objects.all().delete()


def sync_greenhouse(apps, schema_editor):
    management.call_command("sync_greenhouse"),


class Migration(migrations.Migration):

    dependencies = [
        ("careers", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(clear_positions, migrations.RunPython.noop),
        migrations.AddField(
            model_name="position",
            name="internal_job_id",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.RunPython(sync_greenhouse, migrations.RunPython.noop),
    ]
