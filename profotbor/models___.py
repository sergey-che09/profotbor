# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CandidatesAccess(models.Model):
    id = models.BigAutoField(primary_key=True)
    access = models.IntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidates_access'


class CandidatesBranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'candidates_branch'


class CandidatesCandidate(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidatenumber = models.IntegerField(db_column='candidateNumber', blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    years = models.IntegerField(blank=True, null=True)
    startday = models.DateField(db_column='startDay', blank=True, null=True)  # Field name made lowercase.
    tests = models.BooleanField(blank=True, null=True)
    questionnaire = models.BooleanField(blank=True, null=True)
    hrdecision = models.BooleanField(db_column='hrDecision', blank=True, null=True)  # Field name made lowercase.
    hrassessmentsheet = models.BooleanField(db_column='hrAssessmentSheet', blank=True, null=True)  # Field name made lowercase.
    securitydecision = models.BooleanField(db_column='securityDecision', blank=True, null=True)  # Field name made lowercase.
    securityassessment_sheet = models.BooleanField(db_column='securityAssessment_sheet', blank=True, null=True)  # Field name made lowercase.
    departmentdecision = models.BooleanField(db_column='departmentDecision', blank=True, null=True)  # Field name made lowercase.
    departmentassessmentsheet = models.BooleanField(db_column='departmentAssessmentSheet', blank=True, null=True)  # Field name made lowercase.
    ceodecision = models.BooleanField(db_column='ceoDecision', blank=True, null=True)  # Field name made lowercase.
    ceoassessmentsheet = models.BooleanField(db_column='ceoAssessmentSheet', blank=True, null=True)  # Field name made lowercase.
    ppesent = models.BooleanField(db_column='ppeSent', blank=True, null=True)  # Field name made lowercase.
    ppedate = models.DateField(db_column='ppeDate', blank=True, null=True)  # Field name made lowercase.
    ppesummary = models.BooleanField(db_column='ppeSummary', blank=True, null=True)  # Field name made lowercase.
    finaldecision = models.BooleanField(db_column='finalDecision', blank=True, null=True)  # Field name made lowercase.
    finaldate = models.DateField(db_column='finalDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    candidatestatus = models.BooleanField(db_column='candidateStatus', blank=True, null=True)  # Field name made lowercase.
    recruitment = models.BooleanField(blank=True, null=True)
    access = models.ForeignKey(CandidatesAccess, models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(CandidatesBranch, models.DO_NOTHING, blank=True, null=True)
    ceo = models.ForeignKey('CandidatesSpecialist', models.DO_NOTHING, blank=True, null=True)
    control = models.ForeignKey('CandidatesControl', models.DO_NOTHING, blank=True, null=True)
    departmentspecialist = models.ForeignKey('CandidatesSpecialist', models.DO_NOTHING, db_column='departmentSpecialist_id', blank=True, null=True)  # Field name made lowercase.
    hrspecialist = models.ForeignKey('CandidatesSpecialist', models.DO_NOTHING, db_column='hrSpecialist_id', blank=True, null=True)  # Field name made lowercase.
    materials = models.ForeignKey('CandidatesMaterials', models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey('CandidatesPosition', models.DO_NOTHING, blank=True, null=True)
    securityspecialist = models.ForeignKey('CandidatesSpecialist', models.DO_NOTHING, db_column='securitySpecialist_id', blank=True, null=True)  # Field name made lowercase.
    subdivision = models.ForeignKey('CandidatesSubdivision', models.DO_NOTHING, blank=True, null=True)
    visibility = models.ForeignKey('CandidatesVisibility', models.DO_NOTHING, blank=True, null=True)
    speciality = models.ForeignKey('CandidatesSpeciality', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidates_candidate'


class CandidatesControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    control = models.CharField(max_length=150)
    controlbr = models.CharField(db_column='controlBr', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'candidates_control'


class CandidatesMaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'candidates_materials'


class CandidatesPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=100)
    positionbr = models.CharField(db_column='positionBr', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'candidates_position'
# Unable to inspect table 'candidates_position_1'
# The error was: ╬╪╚┴╩└:  эхЄ фюёЄєяр ъ ЄрсышЎх candidates_position_1


class CandidatesSpecialist(models.Model):
    id = models.BigAutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    branch = models.ForeignKey(CandidatesBranch, models.DO_NOTHING)
    control = models.ForeignKey(CandidatesControl, models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey(CandidatesPosition, models.DO_NOTHING)
    subdivision = models.ForeignKey('CandidatesSubdivision', models.DO_NOTHING, blank=True, null=True)
    access_level = models.ForeignKey(CandidatesAccess, models.DO_NOTHING)
    admin = models.BooleanField()
    created = models.DateField()
    description = models.CharField(max_length=300)
    user = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'candidates_specialist'


class CandidatesSpeciality(models.Model):
    id = models.BigAutoField(primary_key=True)
    speciality = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'candidates_speciality'


class CandidatesSubdivision(models.Model):
    id = models.BigAutoField(primary_key=True)
    subdivision = models.CharField(max_length=150)
    subdivisionbr = models.CharField(db_column='subdivisionBr', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'candidates_subdivision'


class CandidatesVisibility(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'candidates_visibility'


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
    id = models.BigAutoField(primary_key=True)
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
# Unable to inspect table 'kandidati'
# The error was: ╬╪╚┴╩└:  эхЄ фюёЄєяр ъ ЄрсышЎх kandidati
# Unable to inspect table 'kandidati_back'
# The error was: ╬╪╚┴╩└:  эхЄ фюёЄєяр ъ ЄрсышЎх kandidati_back
# Unable to inspect table 'ърэфшфрЄ√'
# The error was: ╬╪╚┴╩└:  эхЄ фюёЄєяр ъ ЄрсышЎх ърэфшфрЄ√
