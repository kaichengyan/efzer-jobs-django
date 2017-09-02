from django.forms import ModelForm
from django.forms.widgets import Input, Textarea
from django.utils.translation import ugettext_lazy as _
from jobs.models import Job


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            'company',
            'location',
            'job_position',
            'department',
            'publisher',
            'submitting_resume',
            'description',
            'requirements',
            'company_description'
        ]
        widgets = {
            'company': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'location': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'job_position': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'department': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'publisher': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'submitting_resume': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'description': Textarea(attrs={'rows': 8, 'class': "mdc-textfield__input"}),
            'requirements': Textarea(attrs={'rows': 8, 'class': "mdc-textfield__input"}),
            'company_description': Textarea(attrs={'rows': 12, 'class': "mdc-textfield__input"}),
        }
        labels = {
            'company': _('单位名称'),
            'location': _('工作城市'),
            'job_position': _('工作职位'),
            'department': _('工作部门'),
            'publisher': _('发布者'),
            'submitting_resume': _('简历投递方式'),
            'description': _('工作描述'),
            'requirements': _('工作要求'),
            'company_description': _('单位介绍'),
        }
