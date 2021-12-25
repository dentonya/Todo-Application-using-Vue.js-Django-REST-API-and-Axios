# Generated by Django 4.0 on 2021-12-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_description', models.CharField(max_length=255)),
                ('work_status', models.CharField(choices=[('worktodo', 'Work To do'), ('workdone', 'Work Done')], default='worktodo', max_length=10)),
            ],
        ),
    ]
