# -*- coding: utf-8 -*-
"""
Do not go gentle into that good night

Created on Sun Oct 21 10:36:34 2018

@author: Kenzo Yan
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=('title','text')