# Generated by Django 3.2.9 on 2021-12-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.IntegerField(default=90, verbose_name='Thời hạn khóa học (ngày)'),
            preserve_default=False,
        ),
    ]
