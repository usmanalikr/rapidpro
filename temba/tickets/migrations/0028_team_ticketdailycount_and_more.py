# Generated by Django 4.0.4 on 2022-04-28 21:42

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import temba.utils.fields
import temba.utils.uuid


class Migration(migrations.Migration):

    dependencies = [
        ("orgs", "0094_alter_org_parent"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tickets", "0027_squashed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=temba.utils.uuid.uuid4, unique=True)),
                ("name", models.CharField(max_length=64, validators=[temba.utils.fields.validate_name])),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TicketDailyCount",
            fields=[
                ("is_squashed", models.BooleanField(default=False)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("count_type", models.CharField(max_length=1)),
                ("scope", models.CharField(max_length=32)),
                ("day", models.DateField()),
                ("count", models.IntegerField()),
            ],
        ),
        migrations.AddIndex(
            model_name="ticketdailycount",
            index=models.Index(
                condition=models.Q(("is_squashed", False)),
                fields=["count_type", "scope", "day"],
                name="tickets_dailycount_unsquashed",
            ),
        ),
        migrations.AlterIndexTogether(
            name="ticketdailycount",
            index_together={("count_type", "scope", "day")},
        ),
        migrations.AddField(
            model_name="team",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="team",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="team",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="teams", to="orgs.org"),
        ),
        migrations.AddField(
            model_name="team",
            name="topics",
            field=models.ManyToManyField(related_name="teams", to="tickets.topic"),
        ),
    ]
