from django.db import models
from django.urls import reverse
import datetime
from datetime import date
from django.views.generic import ListView
from django.db import connection


class Position(models.Model):
    position = models.CharField(
        max_length=100,
        verbose_name='Должность'
    )

    positionBr = models.CharField(
        max_length=10,
        verbose_name='Должность кратко'
    )

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['position']


class Branch(models.Model):
    branch = models.CharField(
        max_length=150,
        verbose_name='Филиал'
    )

    def __str__(self):
        return self.branch

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Control(models.Model):
    control = models.CharField(
        max_length=150,
        verbose_name='Управление'
    )

    controlBr = models.CharField(
        max_length=10,
        verbose_name='Управление кратко'
    )

    def __str__(self):
        return self.control

    class Meta:
        verbose_name = 'Управление'
        verbose_name_plural = 'Управления'
        ordering = ['control']


class Subdivision(models.Model):
    subdivision = models.CharField(
        max_length=150,
        verbose_name='Подразделение'
    )

    subdivisionBr = models.CharField(
        max_length=150,
        verbose_name='Подразделение кратко'
    )

    def __str__(self):
        return self.subdivision

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['subdivision']


class Access(models.Model):
    access = models.IntegerField(
        verbose_name='Уровень доступа'
    )
    description = models.CharField(
        max_length=200,
        help_text="Опасание",
        blank=True,
        null=True,
        verbose_name='Опасание'
    )

    def __str__(self):
        return str(self.access)

    class Meta:
        verbose_name = 'Уровень доступа'
        verbose_name_plural = 'Уровни доступа'


class Speciality(models.Model):
    speciality = models.CharField(
        max_length=150,
        verbose_name='Специальность'
    )

    def __str__(self):
        return str(self.speciality)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['speciality']


class Specialist(models.Model):
    surname = models.CharField(
        max_length=50,
        help_text="Иванов",
        verbose_name='Фамилия'
    )
    name = models.CharField(
        max_length=50,
        help_text="Иван",
        verbose_name='Имя'
    )
    patronymic = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        help_text="Иванович",
        verbose_name='Отчество, если имеется'

    )
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        verbose_name='Должность',
        help_text="Выберите должность"
    )
    branch = models.ForeignKey(
        Branch,
        on_delete=models.PROTECT,
        verbose_name='Филиал',
        help_text="Выберите филиал"
    )
    control = models.ForeignKey(
        Control,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Управление',
        help_text="Выберите управление"
    )
    subdivision = models.ForeignKey(
        Subdivision,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Подразделение',
        help_text="Выберите подразделение"

    )
    admin = models.BooleanField(
        default='False',
        verbose_name='Администратор'
    )
    access_level = models.ForeignKey(
        Access,
        on_delete=models.PROTECT,
        verbose_name='Уровень доступа'
    )
    created = models.DateField()
    user = models.BooleanField(
        default='False',
        verbose_name='Пользователь'
    )
    description = models.CharField(
        max_length=300,
        help_text="Коментарии",
        verbose_name='Описание'
    )

    def __str__(self):
        return str('{} {:.1}. {:.1}. - {}'.format(self.surname, self.name, self.patronymic, self.position))

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['surname']


class Materials(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Имя файла",
        verbose_name='Имя файла'
    )

    # path = models.FilePathField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Visibility(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локальные права'
        verbose_name_plural = 'Локальные права'


class Candidate(models.Model):
    BOOL_CHOICES = ((True, 'Да'), (False, 'Нет'))
    BOOL_PPE_CHOICES = ((True, 'Плюс'), (False, 'Минус'))
    BOOL_FINISH_CHOICES = ((True, 'Принять'), (False, 'Отказать'))
    BOOL_STATUS_CHOICES = ((True, 'Завершено'), (False, 'В работе'))

    candidateNumber = models.IntegerField(
        blank=True,
        null=True,
        help_text="1234567",
        verbose_name='Номер кандидата'
    )
    surname = models.CharField(
        max_length=50,
        help_text="Иванов",
        verbose_name='Фамилия'
    )
    name = models.CharField(
        max_length=50,
        help_text="Иван",
        verbose_name='Имя'
    )
    patronymic = models.CharField(
        max_length=50,
        help_text="Иванович",
        blank=True,
        null=True,
        verbose_name='Отчество, если имеется'
    )
    phone = models.CharField(
        max_length=20,
        help_text="+7 (987) 123-45-67",
        verbose_name='Номер тел.'
    )
    email = models.EmailField(
        blank=True,
        null=True,
        help_text="mailbox@mail.com",
        verbose_name='Email'
    )
    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения'
    )
    years = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Полных лет'
    )
    position = models.ForeignKey(
        Position,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Должность',
        help_text="Выберите должность"
    )
    speciality = models.ForeignKey(
        Speciality,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Специальность',
        help_text="Выберите специальность"
    )
    branch = models.ForeignKey(
        Branch,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Филиал',
        help_text="Выберите филиал"
    )
    control = models.ForeignKey(
        Control,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Управление',
        help_text="Выберите управление"
    )
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.PROTECT,
        verbose_name='Подразделение',
        help_text="Выберите подразделение",
        blank=True,
        null=True
    )
    startDay = models.DateField(
        verbose_name='Начало работы'
    )
    tests = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Тесты'
    )
    questionnaire = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Анкета'
    )
    hrSpecialist = models.ForeignKey(
        Specialist,
        related_name='hrSpecialist',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Специалист УРП',
        help_text="Выберите сотрудника"
    )
    hrDecision = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Решение УРП'
    )
    hrAssessmentSheet = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Лист оценки УРП'
    )
    securitySpecialist = models.ForeignKey(
        Specialist,
        related_name='securitySpecialist',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Специалист СБ',
        help_text="Выберите сотрудника"
    )
    securityDecision = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Решение СБ'
    )
    securityAssessment_sheet = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Лист оценки СБ'
    )
    departmentSpecialist = models.ForeignKey(
        Specialist,
        related_name='departmentSpecialist',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Специалист подразделения',
        help_text="Выберите сотрудника"
    )
    departmentDecision = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Решение подразделения'
    )
    departmentAssessmentSheet = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Лист оценки подразделения'
    )
    ceo = models.ForeignKey(
        Specialist,
        related_name='ceo',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Генеральный директор/ЗГД',
        help_text="Выберите сотрудника"
    )
    ceoDecision = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Решение ГД/ЗГД'
    )
    ceoAssessmentSheet = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Лист оценки ГД/ЗГД'
    )
    # photo = models.FilePathField(
    #     blank=True,
    #     null=True,
    #     help_text="Выберите фотографию"
    # )
    ppeSent = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Направление на ПФО'
    )
    ppeDate = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата ПФО'
    )
    ppeSummary = models.BooleanField(
        # choices=BOOL_PPE_CHOICES,
        blank=True,
        null=True,
        verbose_name='Итог ПФО'
    )
    finalDecision = models.BooleanField(
        # choices=BOOL_FINISH_CHOICES,
        blank=True,
        null=True,
        verbose_name='Итоговое решение'
    )
    finalDate = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата итогового решения'
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Примечания'
    )
    remarks = models.TextField(
        blank=True,
        null=True,
        verbose_name='Замечания'
    )
    candidateStatus = models.BooleanField(
        choices=BOOL_STATUS_CHOICES,
        blank=True,
        null=True,
        verbose_name='Статус кандидата'
    )
    recruitment = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='На приём'
    )
    materials = models.ForeignKey(
        Materials,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Материалы'
    )
    access = models.ForeignKey(
        Access,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Доступ'
    )
    visibility = models.ForeignKey(
        Visibility,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Видимость'
    )

    def __str__(self):
        return str('{} {:.1}. {:.1}. -  на должность:  {}'.format(self.surname, self.name, self.patronymic,
                                                                  self.position))

    def fio(self):
        return str('{} {:.1}. {:.1}.'.format(self.surname, self.name, self.patronymic))

    def phoneNumber(self):
        # return str('+7-{}-{}-{}-{}'.format(self.phone[0:3], self.phone[3:6], self.phone[6:8], self.phone[8:10]))
        newTelList = [''.join(filter(str.isdigit, str(self.phone)))]
        if self.phone:
            telNumber = ''.join(
                [('+7 ({}) {}-{}-{}'.format(tel[0:3], tel[3:6], tel[6:8], tel[8:10])) for tel in newTelList])
            return (telNumber)
        return ''

    @property
    def calculate_age(self):
        if self.birthday:
            today = date.today()
            return today.year - self.birthday.year - (
                        (today.month, today.day) < (self.birthday.month, self.birthday.day))
        return ''

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'

# def display_subdivision(self):
#     return ', '.join([subdivision.id for ])


class ReportStatus(models.Model):
    id = models.CharField(
        max_length=20,
        primary_key=True
    )
    branch = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Филиал'
    )
    control = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Управление'
    )
    subdivision = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Подразделение'
    )
    position = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Должность'
    )
    candidateName = models.TextField(
        blank=True,
        null=True,
        verbose_name='ФИО Кандидата'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон'
    )
    startDay = models.DateField(
        verbose_name='Начало работы'
    )
    ppeDate = models.DateField(
        verbose_name='Дата ПФО'
    )
    remarks = models.TextField(
        blank=True,
        null=True,
        verbose_name='Примечание',
    )

    class Meta:
        managed = False
        db_table = 'candidates_report'
        verbose_name = 'Отчет "В работе"'
        verbose_name_plural = 'Отчет "В работе"'

    @classmethod
    def refresh_view(cl):
        with connection.cursor() as cursor:
            cursor.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY candidates_report")


class ViewStatus(models.Model):
    BOOL_STATUS_CHOICES = ((True, "Завершено"), (False, 'В работе'))

    id = models.CharField(
        max_length=20,
        primary_key=True
    )
    candidateStatus = models.BooleanField(
        choices=BOOL_STATUS_CHOICES,
        blank=True,
        null=True,
        verbose_name='Статус'
    )
    candidateNumber = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Номер'
    )

    candidateName = models.TextField(
        blank=True,
        null=True,
        verbose_name='ФИО Кандидата'
    )

    branch = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Филиал'
    )
    control = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Упр.'
    )
    subdivision = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Подр.'
    )
    position = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Должность'
    )
    speciality = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Специальность'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон'
    )
    tests = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Тесты'
    )
    hrDecision = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='УРП'
    )
    securityDecision = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='СБ'
    )
    securityAssessment_sheet = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Лист СБ'
    )
    departmentDecision = models.BooleanField(
        blank=True,
        null=True,
        verbose_name='Подразд.'
    )
    positionBr = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Должн.'
    )

    class Meta:
        managed = False
        db_table = 'candidates_view'
        verbose_name = 'Список кандидатов'
        verbose_name_plural = 'Список кандидатов'

    @classmethod
    def refresh_view(cl):
        with connection.cursor() as cursor:
            cursor.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY candidates_view")




