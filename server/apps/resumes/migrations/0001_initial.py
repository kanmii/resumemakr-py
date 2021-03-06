# Generated by Django 2.2.6 on 2019-11-02 15:02

import django.contrib.postgres.fields.citext
import django.db.models.deletion
import ulid2
from django.db import migrations, models

from server.migration_utils import add_fkey, create_index


class Migration(migrations.Migration):

    initial = True

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.RunSQL(
            """
                CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;
            """
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "school",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "course",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "from_date",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "to_date",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                ("index", models.IntegerField()),
            ],
            options={"db_table": "education"},
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("position", models.TextField(blank=True, null=True)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "from_date",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "to_date",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                ("index", models.IntegerField()),
            ],
            options={"db_table": "experiences"},
        ),
        migrations.CreateModel(
            name="Resumes",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", django.contrib.postgres.fields.citext.CITextField()),
                ("description", models.TextField(blank=True, null=True)),
                ("inserted_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="accounts.User",
                    ),
                ),
            ],
            options={"db_table": "resumes"},
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("index", models.IntegerField()),
                (
                    "resume",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Resumes",
                    ),
                ),
            ],
            options={"db_table": "skills"},
        ),
        migrations.CreateModel(
            name="SupplementarySkill",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "description",
                    django.contrib.postgres.fields.citext.CITextField(),
                ),  # noqa
                (
                    "level",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                ("inserted_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Resumes",
                    ),
                ),
            ],
            options={"db_table": "supplementary_skills"},
        ),
        migrations.CreateModel(
            name="SpokenLanguage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "description",
                    django.contrib.postgres.fields.citext.CITextField(),
                ),  # noqa
                (
                    "level",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                ("inserted_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Resumes",
                    ),
                ),
            ],
            options={"db_table": "spoken_languages"},
        ),
        migrations.CreateModel(
            name="SkillAchievement",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("text", models.TextField()),
                (
                    "owner",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Skill",
                    ),
                ),
            ],
            options={"db_table": "skills_achievements"},
        ),
        migrations.CreateModel(
            name="ResumeHobby",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("text", models.TextField()),
                (
                    "owner",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Resumes",
                    ),
                ),
            ],
            options={"db_table": "resumes_hobbies"},
        ),
        migrations.CreateModel(
            name="PersonalInfo",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "last_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "profession",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                ("address", models.TextField(blank=True, null=True)),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),  # noqa
                (
                    "phone",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "photo",
                    models.CharField(blank=True, max_length=255, null=True),
                ),  # noqa
                (
                    "date_of_birth",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Resumes",
                    ),
                ),
            ],
            options={"db_table": "personal_info"},
        ),
        migrations.CreateModel(
            name="ExperienceAchievement",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("text", models.TextField()),
                (
                    "owner",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Experience",
                    ),
                ),
            ],
            options={"db_table": "experiences_achievements"},
        ),
        migrations.AddField(
            model_name="experience",
            name="resume",
            field=models.ForeignKey(
                db_constraint=False,
                db_index=False,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="resumes.Resumes",
            ),
        ),
        migrations.CreateModel(
            name="EducationAchievement",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=ulid2.generate_ulid_as_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("text", models.TextField()),
                (
                    "owner",
                    models.ForeignKey(
                        db_constraint=False,
                        db_index=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resumes.Education",
                    ),
                ),
            ],
            options={"db_table": "education_achievements"},
        ),
        migrations.AddField(
            model_name="education",
            name="resume",
            field=models.ForeignKey(
                db_constraint=False,
                db_index=False,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="resumes.Resumes",
            ),
        ),
        migrations.AddIndex(
            model_name="skill",
            index=models.Index(
                fields=["resume"], name="skills_resumes_id_index"
            ),  # noqa
        ),
        migrations.AddIndex(
            model_name="resumes",
            index=models.Index(fields=["user"], name="resumes_user_id_index"),
        ),
        migrations.AddIndex(
            model_name="resumehobby",
            index=models.Index(
                fields=["owner"], name="resumes_hobbies_owner_id_index"
            ),  # noqa
        ),
        migrations.AddIndex(
            model_name="personalinfo",
            index=models.Index(
                fields=["resume"], name="personal_info_resume_id_index"
            ),  # noqa
        ),
        migrations.AddIndex(
            model_name="experience",
            index=models.Index(
                fields=["resume"], name="experiences_resume_id_index"
            ),  # noqa
        ),
        migrations.AddIndex(
            model_name="education",
            index=models.Index(
                fields=["resume"], name="education_resume_id_index"
            ),  # noqa
        ),
        migrations.RunSQL(
            f"""
                CREATE UNIQUE INDEX resumes_user_id_title_index
                ON resumes(user_id, title);

                CREATE INDEX education_achievements_owner_id_index
                ON education_achievements(owner_id);

                CREATE INDEX experiences_achievements_owner_id_index
                ON experiences_achievements(owner_id);

                CREATE INDEX skills_achievements_owner_id_index
                ON skills_achievements(owner_id);

                CREATE UNIQUE INDEX spoken_languages_owner_id_index
                ON spoken_languages(owner_id);

                CREATE UNIQUE INDEX spoken_languages_description_owner_id_index
                ON spoken_languages(description, owner_id);

                CREATE UNIQUE INDEX
                supplementary_skills_description_owner_id_index
                ON supplementary_skills(description, owner_id);

                {add_fkey("resumes", "user_id", "users", "id")}

                {add_fkey("education", "resume_id", "resumes", "id")}

                {add_fkey(
                    "education_achievements", "owner_id", "education", "id"
                )}

                {add_fkey("experiences", "resume_id", "resumes", "id")}

                {add_fkey(
                    "experiences_achievements", "owner_id", "experiences", "id"
                )}

                {add_fkey("personal_info", "resume_id", "resumes", "id")}

                {add_fkey("resumes_hobbies", "owner_id", "resumes", "id")}

                {add_fkey("skills", "resume_id", "resumes", "id")}

                {add_fkey("skills_achievements", "owner_id", "skills", "id")}

                {add_fkey("spoken_languages", "owner_id", "resumes", "id")}

                {add_fkey("supplementary_skills", "owner_id", "resumes")}

                {create_index("supplementary_skills", "owner_id")}
            """
        ),
    ]
