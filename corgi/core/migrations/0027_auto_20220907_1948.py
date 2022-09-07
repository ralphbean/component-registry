# Generated by Django 3.2.15 on 2022-09-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0026_get_or_create_unique_constraints_for_null_parent"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="componentnode",
            name="core_compon_type_1f6187_idx",
        ),
        migrations.AddIndex(
            model_name="componentnode",
            index=models.Index(fields=["type"], name="core_compon_type_b33d5b_idx"),
        ),
        migrations.AddIndex(
            model_name="componentnode",
            index=models.Index(fields=["parent"], name="core_compon_parent__2ef718_idx"),
        ),
        migrations.AddIndex(
            model_name="componentnode",
            index=models.Index(fields=["purl"], name="core_compon_purl_bf2311_idx"),
        ),
    ]
