# Generated by Django 2.1.7 on 2019-03-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerLogin',
            fields=[
                ('idcustomer_login', models.AutoField(primary_key=True, serialize=False)),
                ('customer_user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_user_password', models.CharField(blank=True, max_length=50, null=True)),
                ('login_create_date', models.DateTimeField(blank=True, null=True)),
                ('last_login_date', models.DateTimeField(blank=True, db_column='Last_login_date', null=True)),
            ],
            options={
                'db_table': 'customer_login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(db_column='customer_ID', primary_key=True, serialize=False)),
                ('c_first_name', models.CharField(blank=True, db_column='C_first_name', max_length=100, null=True)),
                ('c_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('c_address', models.CharField(blank=True, max_length=500, null=True)),
                ('c_city', models.CharField(blank=True, max_length=45, null=True)),
                ('c_state', models.CharField(blank=True, max_length=45, null=True)),
                ('c_zip', models.CharField(blank=True, max_length=20, null=True)),
                ('c_country', models.CharField(blank=True, max_length=50, null=True)),
                ('c_email', models.CharField(blank=True, max_length=100, null=True)),
                ('c_mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('c_office_number', models.CharField(blank=True, max_length=20, null=True)),
                ('c_create_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrugReimbursements',
            fields=[
                ('dr_r_id', models.AutoField(primary_key=True, serialize=False)),
                ('units_reimbursed', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('number_of_rx', models.IntegerField(blank=True, null=True)),
                ('total_amt_reimbursed', models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True)),
                ('mcd_amt_reimbursed', models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True)),
                ('non_mcd_amt_reimbursed', models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True)),
                ('service_state', models.CharField(blank=True, max_length=45, null=True)),
                ('s_latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('s_longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('s_location', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'drug_reimbursements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrugUtilization',
            fields=[
                ('drug_u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('service_year', models.CharField(blank=True, max_length=20, null=True)),
                ('service_quarter', models.IntegerField(blank=True, null=True)),
                ('quarter_begin', models.CharField(blank=True, max_length=20, null=True)),
                ('quarter_begin_date', models.DateTimeField(blank=True, null=True)),
                ('supression_used', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'drug_utilization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HcpInformation',
            fields=[
                ('hcp_id', models.IntegerField(db_column='HCP_ID')),
                ('f_name', models.CharField(blank=True, db_column='F_Name', max_length=45, null=True)),
                ('l_name', models.CharField(blank=True, db_column='L_Name', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=45, null=True)),
                ('work_number', models.CharField(blank=True, db_column='Work_Number', max_length=20, null=True)),
                ('fax_number', models.CharField(blank=True, db_column='FAX_Number', max_length=20, null=True)),
                ('cell_number', models.CharField(blank=True, db_column='CELL_Number', max_length=20, null=True)),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'hcp_information',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HcpLocation',
            fields=[
                ('hcp_loc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('speciality', models.CharField(blank=True, max_length=200, null=True)),
                ('hcp_office_name', models.CharField(blank=True, db_column='hcp_Office_name', max_length=2000, null=True)),
                ('hcp_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('hcp_city', models.CharField(blank=True, max_length=200, null=True)),
                ('hcp_zip', models.CharField(blank=True, max_length=20, null=True)),
                ('hcp_country', models.CharField(blank=True, db_column='hcp_Country', max_length=50, null=True)),
                ('hcp_office_number', models.CharField(blank=True, max_length=20, null=True)),
                ('hcp_office_fax', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'hcp_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HcpUtilization',
            fields=[
                ('hcp_u_id', models.AutoField(db_column='HCP_U_ID', primary_key=True, serialize=False)),
                ('hcp_pac_id', models.CharField(blank=True, max_length=100, null=True)),
                ('hcp_hcpcs_code', models.CharField(blank=True, db_column='hcp_HCPCS_Code', max_length=50, null=True)),
                ('hcp_code_description', models.CharField(blank=True, db_column='hcp_Code_description', max_length=500, null=True)),
                ('hcp_service_count', models.CharField(blank=True, max_length=10, null=True)),
                ('hcp_beneficiary_count', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'hcp_utilization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicareDrugs',
            fields=[
                ('m_dr_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_utilization_type', models.CharField(blank=True, max_length=45, null=True)),
                ('labeler_code', models.CharField(blank=True, max_length=20, null=True)),
                ('product_code', models.CharField(blank=True, max_length=20, null=True)),
                ('package_size', models.IntegerField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('md_create_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'medicare_drugs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Useraccount',
            fields=[
                ('iduseraccount', models.IntegerField(db_column='idUserAccount', primary_key=True, serialize=False)),
                ('ua_f_name', models.CharField(blank=True, db_column='UA_F_Name', max_length=45, null=True)),
                ('ua_l_name', models.CharField(blank=True, db_column='UA_L_Name', max_length=45, null=True)),
                ('ua_email', models.CharField(blank=True, db_column='UA_Email', max_length=45, null=True)),
                ('ua_user_name', models.CharField(blank=True, db_column='UA_User_Name', max_length=45, null=True)),
                ('ua_password', models.CharField(blank=True, db_column='UA_Password', max_length=45, null=True)),
            ],
            options={
                'db_table': 'useraccount',
                'managed': False,
            },
        ),
    ]