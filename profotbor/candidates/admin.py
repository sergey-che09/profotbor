from django.contrib import admin
from .models import Position, Speciality, Branch, Control, Subdivision, Access, Specialist, Materials, Visibility, \
    Candidate, ReportStatus, ViewStatus
import datetime
from datetime import date
from import_export.admin import ExportActionMixin

# admin.site.register(Position)
admin.site.register(Branch)
admin.site.register(Speciality)
# admin.site.register(Subdivision)
admin.site.register(Access)
# admin.site.register(Specialist)
admin.site.register(Materials)
admin.site.register(Visibility)
#admin.site.register(ReportStatus)

# admin.site.register(Candidate)


@admin.register(ReportStatus)
class ReportStatus(ExportActionMixin, admin.ModelAdmin):
    list_display = ('branch', 'control', 'subdivision', 'position', 'candidateName', 'phone', 'startDay', 'ppeDate')
    readonly_fields = ('id', 'branch', 'control', 'subdivision', 'position', 'candidateName', 'phone', 'startDay', 'ppeDate', 'remarks')


@admin.register(ViewStatus)
class ViewStatus(ExportActionMixin, admin.ModelAdmin):
    list_display = ('candidateNumber', 'candidateStatus', 'candidateName', 'branch', 'control', 'subdivision', 'positionBr', 'speciality',
                    'phone', 'tests', 'hrDecision', 'securityDecision', 'securityAssessment_sheet', 'departmentDecision')
    list_filter = ('branch', 'subdivision')
    readonly_fields = ('id', 'candidateNumber', 'candidateStatus', 'candidateName', 'branch', 'control', 'subdivision', 'positionBr', 'speciality',
                    'phone', 'tests', 'hrDecision', 'securityDecision', 'securityAssessment_sheet', 'departmentDecision', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('positionBr', 'position',)


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'subdivision', 'control', 'description')
    list_filter = ('subdivision', 'branch')
    fields = [('access_level', 'user', 'admin', 'created',), 'surname', 'name', 'patronymic',
              ('position', 'subdivision', 'control', 'branch'), ]


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('subdivisionBr', 'subdivision',)


@admin.register(Control)
class ContrtolAdmin(admin.ModelAdmin):
    list_display = ('controlBr', 'control',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    model = Candidate
    # list_display = (['__str__'])
    list_display = ([
        'candidateStatus',
        'startDay',
        'fio',
        'phoneNumber',
        # 'email',
        'branch',
        'subdivision',
        'tests',
        'questionnaire',
        'hrDecision',
        'departmentDecision',
        'securityDecision',
        'ceoDecision',
        'ppeSent',
        'ppeSummary',
        'recruitment',
        'calculate_age',
    ])
    search_fields = (
        'surname__startswith',
    )
    fields = [('startDay', 'candidateNumber', 'candidateStatus',),
              'surname',
              'name',
              'patronymic',
              ('phone', 'email', ),
              'birthday',
              ('position', 'speciality', 'subdivision',),
              ('control', 'branch', ),
              ('tests', 'questionnaire',),
              ('hrSpecialist', 'hrDecision', 'hrAssessmentSheet',),
              ('securitySpecialist', 'securityDecision', 'securityAssessment_sheet',),
              ('departmentSpecialist', 'departmentDecision', 'departmentAssessmentSheet',),
              ('ceo', 'ceoDecision', 'ceoAssessmentSheet',),
              ('ppeDate', 'ppeSent', 'ppeSummary',),
              ('finalDate', 'finalDecision',),
              'notes',
              'remarks',
              ]

    # def calculate_age(self, obj: Candidate) -> str:
    #     today = date.today()
    #     age = today.year - obj.birthday.dt
    #     full_year_passed = (today.month, today.day) < (obj.birthday.dt.month, obj.birthday.dt.day)
    #     if full_year_passed:
    #         age -= 1
    #     return f"{age}"



