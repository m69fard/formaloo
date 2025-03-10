# Generated by Django 5.1.6 on 2025-02-25 14:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('rejected', 'Rejected')], db_index=True, default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='app',
            name='title',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AddIndex(
            model_name='app',
            index=models.Index(fields=['status', 'created_at'], name='appstore_ap_status_9b91fd_idx'),
        ),
        migrations.AddIndex(
            model_name='app',
            index=models.Index(fields=['owner', 'created_at'], name='appstore_ap_owner_i_c17784_idx'),
        ),
    ]
