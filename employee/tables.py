import django_tables2 as tables
from .models import DmsUser, Department
from django_tables2 import A

class DmsUserTable(tables.Table):
    # username = tables.LinkColumn("employee_change", args=[A("pk")])
    class Meta:
        model = DmsUser
        fields = ['username', 'first_name', 'last_name', 'email', 'department', 'groups']


class DepartmentTable(tables.Table):
    # dept_no = tables.LinkColumn("department_detail", args=[A("pk")])
    employees = tables.LinkColumn("dept_emps", args=[A("pk")])
    # edit = tables.LinkColumn("department_change", text='edit', args=[A("pk")])
    class Meta:
        model = Department
        fields = ['dept_no', 'dept_name', 'employees', 'reviewers', 'approver']


class DeptEmpsTable(tables.Table):
    # username = tables.LinkColumn("")
    class Meta:
        model = DmsUser
        fields = ['username', 'first_name', 'last_name', 'email', 'department']
