# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_added = models.DateField()

    class Meta:
        managed = False
        db_table = 'Cart'


class Cartitem(models.Model):
    quantity = models.IntegerField()
    active = models.IntegerField()
    cart_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CartItem'


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
    last_name = models.CharField(max_length=150)
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


class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_added = models.DateField()

    class Meta:
        managed = False
        db_table = 'cart'


class Cartitem(models.Model):
    quantity = models.IntegerField()
    active = models.IntegerField()
    cart = models.ForeignKey(Cart, models.DO_NOTHING)
    product = models.ForeignKey('ShopProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cartitem'


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
    m_dr = models.ForeignKey('MedicareDrugs', models.DO_NOTHING, blank=True, null=True)
    service_year = models.CharField(max_length=20, blank=True, null=True)
    service_quarter = models.IntegerField(blank=True, null=True)
    quarter_begin = models.CharField(max_length=20, blank=True, null=True)
    quarter_begin_date = models.DateTimeField(blank=True, null=True)
    supression_used = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_utilization'


class DupNpi(models.Model):
    npi = models.TextField(db_column='NPI', blank=True, null=True)  # Field name made lowercase.
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dup_npi'


class FullUsHcp(models.Model):
    hcp_firstname = models.TextField(db_column='HCP_FirstName', blank=True, null=True)  # Field name made lowercase.
    hcp_lastname = models.TextField(db_column='HCP_LastName', blank=True, null=True)  # Field name made lowercase.
    hcp_address1 = models.TextField(db_column='HCP_Address1', blank=True, null=True)  # Field name made lowercase.
    hcp_address2 = models.TextField(db_column='HCP_Address2', blank=True, null=True)  # Field name made lowercase.
    hcp_city = models.TextField(db_column='HCP_City', blank=True, null=True)  # Field name made lowercase.
    hcp_state = models.TextField(db_column='HCP_State', blank=True, null=True)  # Field name made lowercase.
    hcp_zip = models.TextField(db_column='HCP_Zip', blank=True, null=True)  # Field name made lowercase.
    hcp_country = models.TextField(db_column='HCP_Country', blank=True, null=True)  # Field name made lowercase.
    hcp_primary_phone = models.TextField(db_column='HCP_Primary_Phone', blank=True, null=True)  # Field name made lowercase.
    license_number = models.TextField(db_column='License_Number', blank=True, null=True)  # Field name made lowercase.
    npi = models.TextField(db_column='NPI', blank=True, null=True)  # Field name made lowercase.
    primary_email = models.TextField(db_column='Primary_Email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'full_us_hcp'


class HcpInformation(models.Model):
    f_name = models.CharField(db_column='F_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    work_number = models.CharField(db_column='Work_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax_number = models.CharField(db_column='FAX_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cell_number = models.CharField(db_column='CELL_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    speciality = models.CharField(max_length=200, blank=True, null=True)
    hcp_office_name = models.CharField(db_column='hcp_Office_name', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    hcp_address = models.CharField(max_length=1000, blank=True, null=True)
    hcp_city = models.CharField(max_length=200, blank=True, null=True)
    hcp_state = models.CharField(max_length=50, blank=True, null=True)
    hcp_zip = models.CharField(max_length=20, blank=True, null=True)
    hcp_country = models.CharField(db_column='hcp_Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hcp_total_service_count = models.IntegerField(blank=True, null=True)
    hcp_total_beneficiary_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcp_information'


class HcpInformation1(models.Model):
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
        db_table = 'hcp_information_1'


class HcpLocation(models.Model):
    hcp_loc_id = models.AutoField(primary_key=True)
    hcp = models.ForeignKey(HcpInformation, models.DO_NOTHING, db_column='HCP_ID', blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(max_length=200, blank=True, null=True)
    hcp_office_name = models.CharField(db_column='hcp_Office_name', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    hcp_address = models.CharField(max_length=1000, blank=True, null=True)
    hcp_city = models.CharField(max_length=200, blank=True, null=True)
    hcp_state = models.CharField(max_length=50, blank=True, null=True)
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
    hcp_service_count = models.IntegerField(blank=True, null=True)
    hcp_beneficiary_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcp_utilization'


class HhandsDhutilization(models.Model):
    drug_u_id = models.AutoField(primary_key=True)
    service_year = models.CharField(max_length=20, blank=True, null=True)
    service_quarter = models.IntegerField(blank=True, null=True)
    quarter_begin = models.CharField(max_length=1000, blank=True, null=True)
    quarter_begin_date = models.CharField(max_length=1000, blank=True, null=True)
    supression_used = models.CharField(max_length=20, blank=True, null=True)
    m_dr = models.ForeignKey('HhandsDrugsheader', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hhands_dhutilization'


class HhandsDrreimbursements(models.Model):
    dr_r_id = models.AutoField(primary_key=True)
    units_reimbursed = models.TextField(blank=True, null=True)
    number_of_rx = models.IntegerField(blank=True, null=True)
    total_amt_reimbursed = models.TextField(blank=True, null=True)
    mcd_amt_reimbursed = models.TextField(blank=True, null=True)
    non_mcd_amt_reimbursed = models.TextField(blank=True, null=True)
    service_state = models.CharField(max_length=45, blank=True, null=True)
    s_latitude = models.TextField(blank=True, null=True)
    s_longitude = models.TextField(blank=True, null=True)
    s_location = models.CharField(max_length=50, blank=True, null=True)
    dr_u = models.ForeignKey(HhandsDhutilization, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hhands_drreimbursements'


class HhandsDrreimtotals(models.Model):
    service_state = models.CharField(max_length=45, blank=True, null=True)
    total_amt_reimbursed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hhands_drreimtotals'


class HhandsDrugsheader(models.Model):
    m_dr_id = models.AutoField(primary_key=True)
    m_utilization_type = models.CharField(max_length=45, blank=True, null=True)
    labeler_code = models.CharField(max_length=20, blank=True, null=True)
    product_code = models.CharField(max_length=20, blank=True, null=True)
    package_size = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=1000, blank=True, null=True)
    md_create_date = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hhands_drugsheader'


class HhandsUser(models.Model):
    user_ptr = models.ForeignKey(AuthUser, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'hhands_user'


class MedicareDrugs(models.Model):
    m_dr_id = models.AutoField(primary_key=True)
    m_utilization_type = models.CharField(max_length=45, blank=True, null=True)
    labeler_code = models.CharField(max_length=20, blank=True, null=True)
    product_code = models.CharField(max_length=20, blank=True, null=True)
    package_size = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=1000, blank=True, null=True)
    md_create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicare_drugs'


class Order(models.Model):
    token = models.CharField(max_length=250)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    emailaddress = models.CharField(db_column='emailAddress', max_length=250)  # Field name made lowercase.
    created = models.DateTimeField()
    billingname = models.CharField(db_column='billingName', max_length=250)  # Field name made lowercase.
    billingaddress1 = models.CharField(db_column='billingAddress1', max_length=250)  # Field name made lowercase.
    billingcity = models.CharField(db_column='billingCity', max_length=250)  # Field name made lowercase.
    billingpostcode = models.CharField(db_column='billingPostcode', max_length=10)  # Field name made lowercase.
    billingcountry = models.CharField(db_column='billingCountry', max_length=200)  # Field name made lowercase.
    shippingname = models.CharField(db_column='shippingName', max_length=250)  # Field name made lowercase.
    shippingaddress1 = models.CharField(db_column='shippingAddress1', max_length=250)  # Field name made lowercase.
    shippingcity = models.CharField(db_column='shippingCity', max_length=250)  # Field name made lowercase.
    shippingpostcode = models.CharField(db_column='shippingPostcode', max_length=10)  # Field name made lowercase.
    shippingcountry = models.CharField(db_column='shippingCountry', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Orderitem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orderitem'


class ShopCategory(models.Model):
    name = models.CharField(unique=True, max_length=250)
    slug = models.CharField(unique=True, max_length=250)
    description = models.TextField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'shop_category'


class ShopProduct(models.Model):
    name = models.CharField(unique=True, max_length=250)
    slug = models.CharField(unique=True, max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100)
    stock = models.IntegerField()
    available = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    category = models.ForeignKey(ShopCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_product'


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
