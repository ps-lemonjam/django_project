from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # 사용하는 모델 정보
        fields = ('title', 'text',) # 사용하는 필드 정보
