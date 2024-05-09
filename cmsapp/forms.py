from   .models   import   DeptModel, StudentModel
from  django import  forms

class DeptForm(forms.ModelForm):
	class Meta:
		model = DeptModel
		fields = "__all__"

class StudentForm(forms.ModelForm):
	class Meta:
		model = StudentModel
		fields = "__all__"



