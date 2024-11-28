from django.forms import ModelForm
from base.models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields ='__all__'
        #["name","description","topic","host"]
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'