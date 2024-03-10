# Generated by Django 4.2.9 on 2024-03-06 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.BooleanField(default=True)),
                ('assay_num', models.CharField(max_length=50)),
                ('mission_num', models.CharField(max_length=50)),
                ('permit_type', models.CharField(max_length=50)),
                ('contractor_name', models.CharField(max_length=50)),
                ('feeder_name', models.CharField(max_length=50)),
                ('voltage_type', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_team_img', models.ImageField(default='img/unknown.png', upload_to='work_team')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violations_img', models.ImageField(default='img/unknown.png', upload_to='violations')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='TUVForEquipmentAndDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TUV_for_equipment_and_driver_img', models.ImageField(default='img/unknown.png', upload_to='TUV_for_equipment_and_driver')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_model_img', models.ImageField(default='img/unknown.png', upload_to='team_model')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_number_img', models.ImageField(default='img/unknown.png', upload_to='subscription_number')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='SourceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_card_img', models.ImageField(default='img/unknown.png', upload_to='source_card')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='SafeWorkProcedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safe_work_procedures_img', models.ImageField(default='img/unknown.png', upload_to='safe_work_procedures')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='SafetyBarrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety_barriers_img', models.ImageField(default='img/unknown.png', upload_to='safety_barriers')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='RiskAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_assessment_img', models.ImageField(default='img/unknown.png', upload_to='risk_assessment')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='ResidenceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Residence_img', models.ImageField(default='img/unknown.png', upload_to='residence')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_card_img', models.ImageField(default='img/unknown.png', upload_to='recipient_card')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='PreworkMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prework_meeting', models.ImageField(default='img/unknown.png', upload_to='prework_meeting')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='PicturesOfSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures_of_site_img', models.ImageField(default='img/unknown.png', upload_to='pictures_of_site')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permit_img', models.ImageField(default='img/unknown.png', upload_to='permits')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='Paramedic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paramedic_img', models.ImageField(default='img/unknown.png', upload_to='paramedic')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='Obstacle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obstacles_img', models.ImageField(default='img/unknown.png', upload_to='obstacles')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_img', models.ImageField(default='img/unknown.png', upload_to='objects')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='MeterCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_capacity_img', models.ImageField(default='img/unknown.png', upload_to='meter_capacity')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='FossilView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fossil_view_img', models.ImageField(default='img/unknown.png', upload_to='fossil_view')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='FirstAid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_aid_img', models.ImageField(default='img/unknown.png', upload_to='first_aid')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='FireExtinguisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fire_extinguisher_img', models.ImageField(default='img/unknown.png', upload_to='fire_extinguisher')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fighter', models.ImageField(default='img/unknown.png', upload_to='fighter')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='DepthOfExcavation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth_of_excavation_img', models.ImageField(default='img/unknown.png', upload_to='depth_of_excavation')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='CutterCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutter_capacity_img', models.ImageField(default='img/unknown.png', upload_to='cutter_capacity')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='CableLength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cable_length_img', models.ImageField(default='img/unknown.png', upload_to='cable_length')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_task_img', models.ImageField(default='img/unknown.png', upload_to='assigned_task')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
        migrations.CreateModel(
            name='ArtificialSecurityCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artificial_security_card_img', models.ImageField(default='img/unknown.png', upload_to='artificial_security_card')),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay')),
            ],
        ),
    ]
