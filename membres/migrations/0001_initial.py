# Generated by Django 4.1.3 on 2022-12-03 19:39

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
            name="Profil",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Photo", models.ImageField(blank=True, upload_to="users_profil/")),
                ("Telephone", models.IntegerField(null=True)),
                ("Adresse1", models.CharField(max_length=200)),
                ("Adresse2", models.CharField(max_length=200)),
                ("Description", models.TextField()),
                (
                    "Region",
                    models.CharField(
                        choices=[
                            ("Dakar", "dakar"),
                            ("Thiès", "thiès"),
                            ("Diourbel", "diourbel"),
                            ("Louga", "louga"),
                            ("Saint-Louis", "st-louis"),
                            ("Kaolack", "kaolack"),
                            ("Fatick", "fatick"),
                            ("Kaffrine", "kaffrine"),
                            ("Sédhiou", "sédhiou"),
                            ("Tambacounda", "tambacounda"),
                            ("Matam", "matam"),
                            ("Ziguinchor", "ziguinchor"),
                            ("Kolda", "Kolda"),
                            ("Kédougou", "kédougou"),
                        ],
                        max_length=11,
                    ),
                ),
                ("Link", models.CharField(max_length=200, null=True)),
                (
                    "Profil_User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
