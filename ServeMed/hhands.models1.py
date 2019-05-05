# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CustomerLogin(models.Model):
    idcustomer_login = models.AutoField(primary_key=True)
    customer_admin = models.ForeignKey('Useraccount', models.DO_NOTHING)
    customer_user_name = models.CharField(max_length=50, blank=True, null=True)
    customer_user_password = models.CharField(max_length=50, blank=True, null=True)
    login_create_date = models.DateTimeField(blank=True, null=True)
    last_login_date = models.DateTimeField(db_column='Last_login_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_login'


class Customers(models.Model):
    customer_id = models.IntegerField(db_column='customer_ID', primary_key=True)  # Field name made lowercase.
    c_first_name = models.CharField(db_column='C_first_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c_last_name = models.CharField(max_length=50, blank=True, null=True)
    c_address = models.CharField(max_length=500, blank=True, null=True)
    c_city = models.CharField(max_length=45, blank=True, null=True)
    c_state = models.CharField(max_length=45, blank=True, null=True)
    c_zip = models.CharField(max_length=20, blank=True, null=True)
    c_country = models.CharField(max_length=50, blank=True, null=True)
    c_email = models.CharField(max_length=100, blank=True, null=True)
    c_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    c_office_number = models.CharField(max_length=20, blank=True, null=True)
    c_create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DrugReimbursements(models.Model):
    dr_r_id = models.AutoField(primary_key=True)
    dr_u = models.ForeignKey('DrugUtilization', models.DO_NOTHING, blank=True, null=True)
    units_reimbursed = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    number_of_rx = models.IntegerField(blank=True, null=True)
    total_amt_reimbursed = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    mcd_amt_reimbursed = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    non_mcd_amt_reimbursed = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    service_state = models.CharField(max_length=45, blank=True, null=True)
    s_latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    s_longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    s_location = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_reimbursements'


class DrugUtilization(models.Model):
    drug_u_id = models.IntegerField(primary_key=True)
    m_dr = models.ForeignKey('MedicareDrungs', models.DO_NOTHING, blank=True, null=True)
    service_year = models.CharField(max_length=20, blank=True, null=True)
    service_quarter = models.IntegerField(blank=True, null=True)
    quarter_begin = models.CharField(max_length=20, blank=True, null=True)
    quarter_begin_date = models.DateTimeField(blank=True, null=True)
    supression_used = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_utilization'


class HcpInformation(models.Model):
    hcp_id = models.IntegerField(db_column='HCP_ID')  # Field name made lowercase.
    f_name = models.CharField(db_column='F_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    work_number = models.CharField(db_column='Work_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax_number = models.CharField(db_column='FAX_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cell_number = models.CharField(db_column='CELL_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcp_information'


class HcpLocation(models.Model):
    hcp_loc_id = models.IntegerField(primary_key=True)
    hcp = models.ForeignKey(HcpInformation, models.DO_NOTHING, db_column='HCP_ID', blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(max_length=200, blank=True, null=True)
    hcp_office_name = models.CharField(db_column='hcp_Office_name', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    hcp_address = models.CharField(max_length=1000, blank=True, null=True)
    hcp_city = models.CharField(max_length=200, blank=True, null=True)
    hcp_zip = models.CharField(max_length=20, blank=True, null=True)
    hcp_country = models.CharField(db_column='hcp_Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hcp_office_number = models.CharField(max_length=20, blank=True, null=True)
    hcp_office_fax = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcp_location'


class HcpUtilization(models.Model):
    hcp_u_id = models.AutoField(db_column='HCP_U_ID', primary_key=True)  # Field name made lowercase.
    hcp = models.ForeignKey(HcpInformation, models.DO_NOTHING, blank=True, null=True)
    hcp_pac_id = models.CharField(max_length=100, blank=True, null=True)
    hcp_hcpcs_code = models.CharField(db_column='hcp_HCPCS_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hcp_code_description = models.CharField(db_column='hcp_Code_description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hcp_service_count = models.CharField(max_length=10, blank=True, null=True)
    hcp_beneficiary_count = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcp_utilization'


class MedicareDrungs(models.Model):
    m_dr_id = models.AutoField(primary_key=True)
    m_utilization_type = models.CharField(max_length=45, blank=True, null=True)
    labeler_code = models.CharField(max_length=20, blank=True, null=True)
    product_code = models.CharField(max_length=20, blank=True, null=True)
    package_size = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=1000, blank=True, null=True)
    md_create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicare_drungs'


class Useraccount(models.Model):
    iduseraccount = models.IntegerField(db_column='idUserAccount', primary_key=True)  # Field name made lowercase.
    ua_f_name = models.CharField(db_column='UA_F_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ua_l_name = models.CharField(db_column='UA_L_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ua_email = models.CharField(db_column='UA_Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ua_user_name = models.CharField(db_column='UA_User_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ua_password = models.CharField(db_column='UA_Password', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccount'
