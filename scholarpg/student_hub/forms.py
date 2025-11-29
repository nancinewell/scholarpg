from django import forms
from .models import Student, Behaviors, Skills, RandomEvents, Miracles

#quick create forms for models
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "image", "charClass", "sp"]

class BehaviorForm(forms.ModelForm):
    class Meta:
        model = Behaviors
        fields = ["title", "desc", "xp", "gp"]

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ["title", "desc", "charClass", "sp", "levelReq"]

class RandomEventForm(forms.ModelForm):
    class Meta:
        model = RandomEvents
        fields = ["title", "desc", "charClass", "sp", "xp", "gp", "randomStudent"]

class MiracleForm(forms.ModelForm):
    class Meta:
        model = Miracles
        fields = ["title", "desc", "sp", "xp", "gp"]