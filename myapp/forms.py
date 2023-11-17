from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de Tarea: ", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Descripción de la tarea:',widget=forms.TextInput(attrs={'class':'input'}))
    project_id = forms.CharField(label="Proyecto", widget=forms.Select)

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del proyecto', max_length=200, widget=forms.TextInput(attrs={'class':'input'}))