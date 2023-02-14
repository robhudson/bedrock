# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 2.2.24 on 2021-11-04 11:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contentful", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contentfulentry",
            old_name="language",
            new_name="locale",
        ),
    ]
