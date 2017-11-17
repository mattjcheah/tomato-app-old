from django import forms

class CountdownForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    due = forms.DateField(label='Due')
