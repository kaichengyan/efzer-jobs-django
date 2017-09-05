from django.forms import ModelForm
from django.forms.widgets import Input, Textarea, RadioSelect
from django.utils.translation import ugettext_lazy as _
from jobs.models import Job


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            'type',
            'company',
            'location',
            'job_position',
            'department',
            'publisher_class',
            'publisher',
            'salary',
            'submitting_resume',
            'description',
            'requirements',
            'company_description'
        ]

        widgets = {
            'type': RadioSelect(attrs={'class': "mdc-radio__native-control", 'required': True}),
            'company': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'location': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'job_position': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'department': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'publisher_class': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'publisher': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'salary': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'submitting_resume': Input(attrs={'class': "mdc-textfield__input", 'required': True}),
            'description': Textarea(attrs={'rows': 8, 'class': "mdc-textfield__input"}),
            'requirements': Textarea(attrs={'rows': 8, 'class': "mdc-textfield__input"}),
            'company_description': Textarea(attrs={'rows': 12, 'class': "mdc-textfield__input"}),
        }

        labels = {
            'type': _('招聘类型'),
            'company': _('单位名称'),
            'location': _('工作城市'),
            'job_position': _('工作职位'),
            'department': _('工作部门'),
            'publisher_class': _('发布者班级'),
            'publisher': _('发布者'),
            'salary': _('薪资'),
            'submitting_resume': _('简历投递方式'),
            'description': _('工作描述'),
            'requirements': _('工作要求'),
            'company_description': _('单位介绍'),
        }
