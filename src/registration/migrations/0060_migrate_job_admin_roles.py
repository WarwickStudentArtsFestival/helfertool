# Generated by Django 3.2.13 on 2022-06-04 13:11

from django.db import migrations


def create_through_relations(apps, schema_editor):
    Job = apps.get_model("registration", "Job")
    JobAdminRoles = apps.get_model("registration", "JobAdminRoles")

    for job in Job.objects.all():
        for admin in job.job_admins.all():
            JobAdminRoles(
                job=job,
                user=admin,
                roles=[
                    "FULL",
                ],
            ).save()


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0059_add_job_admin_roles"),
    ]

    operations = [
        migrations.RunPython(create_through_relations, reverse_code=migrations.RunPython.noop),
    ]