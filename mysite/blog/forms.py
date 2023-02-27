from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                                widget=forms.Textarea)