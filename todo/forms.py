from django.forms import ModelForm
from .models import Todo
   
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','quantity', 'memo', 'important',  'photo_main', 'need_by_date']