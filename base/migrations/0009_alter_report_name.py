# Generated by Django 4.1.4 on 2022-12-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_room_like_count_alter_room_message_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(choices=[('Spam', 'Spam'), ('Terrorism', 'Terrorism'), ('Discrimination', 'Discrimination'), ('Misinformation', 'Misinformation'), ('Public Shaming', 'Public Shaming'), ('Illegal or Dangerous', 'Illegial or Dangerous'), ('Sexual Harrassment', 'Sexual Harassment'), ('Else', 'Else')], default='Spam', max_length=50),
        ),
    ]
