# Generated by Django 5.1.4 on 2024-12-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_alter_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]