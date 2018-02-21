from django.forms import ModelForm
from django import forms
from herberg.models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ["image"]

