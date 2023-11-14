from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de Tarea: ", max_length=200)
    description = forms.CharField(label='Descripción de la tarea:',widget=forms.Textarea)
    project_id = forms.CharField(label="Proyecto", widget=forms.Select)