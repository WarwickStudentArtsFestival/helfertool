# Generated by Django 3.1.4 on 2020-12-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0018_specialbadges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialbadges',
            name='badges',
            field=models.ManyToManyField(blank=True, related_name='_specialbadges_badges_+', to='badges.Badge'),
        ),
    ]