from django import forms

from .models import Todo


class DateInput(forms.DateInput):
    input_type = "date"


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "resolved"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "due_date": DateInput(),
        }
        labels = {"resolved": "Mark as resolved"}
