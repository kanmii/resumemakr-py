# -*- coding: utf-8 -*-

from django.db import models
from ulid2 import generate_ulid_as_uuid
from django.contrib.postgres.fields import CITextField

from server.apps.accounts.models import User


class TextOnly(models.Model):
    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)
    text = models.TextField()

    class Meta:
        abstract = True


class Resume(models.Model):  # type: ignore[disallow_any_explicit] # noqa F821
    class Meta:
        db_table = "resumes"

        indexes = [models.Index(fields=("user",), name="resumes_user_id_index")]

    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)
    title = CITextField()
    description = models.TextField(blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, models.DO_NOTHING, db_constraint=False, db_index=False
    )

    def __str__(self):
        return self.title


class Education(models.Model):
    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)
    index = models.IntegerField()
    resume = models.ForeignKey(
        Resume, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    school = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.CharField(max_length=255, blank=True, null=True)
    to_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "education"

        indexes = [
            models.Index(fields=("resume",), name="education_resume_id_index")
        ]  # noqa


class EducationAchievement(TextOnly):
    owner = models.ForeignKey(
        Education, models.DO_NOTHING, db_constraint=False, db_index=False
    )

    class Meta:
        db_table = "education_achievements"


class Experience(models.Model):
    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)
    index = models.IntegerField()
    resume = models.ForeignKey(
        Resume, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    position = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.CharField(max_length=255, blank=True, null=True)
    to_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "experiences"

        indexes = [
            models.Index(fields=("resume",), name="experiences_resume_id_index")
        ]  # noqa


class ExperienceAchievement(TextOnly):
    owner = models.ForeignKey(
        Experience, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    class Meta:
        db_table = "experiences_achievements"


class PersonalInfo(models.Model):
    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)

    resume = models.ForeignKey(
        Resume,
        models.DO_NOTHING,
        db_index=False,
        db_constraint=False,
        related_name="personal_info",
    )

    class Meta:
        db_table = "personal_info"

        indexes = [
            models.Index(
                fields=("resume",), name="personal_info_resume_id_index"
            )  # noqa
        ]


class ResumeHobby(TextOnly):
    owner = models.ForeignKey(
        Resume, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    class Meta:
        db_table = "resumes_hobbies"

        indexes = [
            models.Index(
                fields=("owner",), name="resumes_hobbies_owner_id_index"
            )  # noqa
        ]


class Skill(models.Model):
    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)
    index = models.IntegerField()
    resume = models.ForeignKey(
        Resume, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "skills"

        indexes = [
            models.Index(fields=("resume",), name="skills_resumes_id_index")
        ]  # noqa


class SkillAchievement(TextOnly):
    owner = models.ForeignKey(
        Skill, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    class Meta:
        db_table = "skills_achievements"


class Ratable(models.Model):  # type: ignore[disallow_any_explicit] # noqa F821
    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)
    description = CITextField()
    level = models.CharField(max_length=255, blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SpokenLanguage(Ratable):  # type: ignore[disallow_any_explicit] # noqa F821
    owner = models.ForeignKey(
        Resume, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    class Meta:
        db_table = "spoken_languages"


class SupplementarySkill(Ratable):  # type: ignore[disallow_any_explicit] # noqa F821
    owner = models.ForeignKey(
        Resume, models.DO_NOTHING, db_index=False, db_constraint=False
    )

    class Meta:
        db_table = "supplementary_skills"
