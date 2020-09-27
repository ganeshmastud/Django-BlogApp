from django import forms
from .models import Post,Category,Comment
from time import sleep
e=None
for i in range(0,5):
    try:
        choices= Category.objects.all().values_list('name','name')
        choice_list=[]

        for item in choices:
            choice_list.append(item)
        e=None
    except Exception as e:
        print(e)
    if e:
        sleep(5)
    else:
        break
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','title_tag','category','author','body','snippet','header_image')
        widgets ={
            'title': forms.TextInput(attrs={'class':     'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'},value:),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','title_tag','body','snippet')
        widgets ={
            'title': forms.TextInput(attrs={'class':     'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),

            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommmentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('name','body')
        widgets ={
            'name': forms.TextInput(attrs={'class':     'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }