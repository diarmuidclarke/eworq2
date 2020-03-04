# Generated by Django 3.0.4 on 2020-03-04 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElevatedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elev_userID', models.CharField(max_length=20)),
                ('elev_user_is_executor', models.BooleanField(default=False)),
                ('elev_user_is_approver', models.BooleanField(default=False)),
                ('elev_user_is_EQA_approver', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='eWORQ_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eWORQ_ID', models.BigIntegerField(verbose_name='eWORQ ID')),
                ('eWORQ_raised_date', models.DateTimeField(verbose_name='date raised')),
                ('eWORQ_requestor_userID', models.CharField(max_length=20)),
                ('eWORQ_project', models.CharField(max_length=50)),
                ('eWORQ_project_desc', models.CharField(max_length=2000)),
                ('eWORQ_copyfiles_src_dir', models.CharField(max_length=2000)),
                ('eWORQ_copyfiles_dest_dir', models.CharField(max_length=2000)),
                ('eWORQ_manualwork_desc', models.CharField(max_length=20000)),
                ('eWORQ_request_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='eWORQ_Rejection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=2000)),
                ('rejector_userID', models.CharField(max_length=20)),
                ('rejection_date', models.DateTimeField(verbose_name='date rejected')),
                ('eworq_id_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eworqapp.eWORQ_Request')),
            ],
        ),
        migrations.CreateModel(
            name='eWORQ_CopyFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=2000)),
                ('eworq_id_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eworqapp.eWORQ_Request')),
            ],
        ),
        migrations.CreateModel(
            name='eWORQ_Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver_userID', models.CharField(max_length=20)),
                ('approval_date', models.DateTimeField(verbose_name='date approved')),
                ('eworq_id_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eworqapp.eWORQ_Request')),
            ],
        ),
    ]