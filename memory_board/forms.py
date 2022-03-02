from django import forms

from .models import Memory


class MemoryForm(forms.ModelForm):
    """Класс формы для воспоминаний"""

    address = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        """Класс настроек формы"""

        model = Memory
        fields = ('title', 'description', 'address')
