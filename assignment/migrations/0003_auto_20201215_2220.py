# Generated by Django 3.1.4 on 2020-12-15 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_executions'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestsubmission',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.question'),
        ),
        migrations.AddField(
            model_name='submission',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.question'),
        ),
    ]
