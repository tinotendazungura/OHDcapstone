# Generated by Django 2.1.5 on 2019-04-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20190408_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('C', 'Closed')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='urgency',
            field=models.CharField(blank=True, choices=[('TP', 'Top Priority'), ('NP', 'Normal Priority'), ('LP', 'Low Priority')], default='NP', help_text='Ticket Priority', max_length=2),
        ),
    ]