from django import forms

class SubmitAdForm(forms.Form):
    ad_title = forms.CharField()
    ad_file = forms.FileField()
    ad_funder = forms.CharField()
    ad_tags = forms.CharField()
    article_url = forms.URLField()

