# Generated by Django 4.2.7 on 2023-12-01 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='balancechange',
            name='staff_member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='initiated_balance_changes', to='community.userprofile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='staff_id',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='balancechange',
            name='transaction_type',
            field=models.CharField(choices=[('CREATE_EVENT', ' Created Event'), ('JOIN_EVENT', ' Joined Event'), ('CREDIT_ISSUED', 'Credit Issued')], max_length=90),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('INSTRUCTOR', 'Instructor'), ('GOVERNMENT', 'Government Official'), ('PUBLIC', 'General Public User'), ('STAFF', 'Staff')], default='PUBLIC', max_length=30),
        ),
    ]
