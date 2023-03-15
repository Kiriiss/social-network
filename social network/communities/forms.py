from django import forms
from communities.models import Community

class CommunityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
        model = Community
        fields = ['name', 'description', 'photo']
        labels = {
            'name': 'Name of Your Community',
            'description': 'Description',
            'photo': 'Upload a Photo for Your Community'
        }
