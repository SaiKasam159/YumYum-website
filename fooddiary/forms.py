from django.forms import ModelForm
from .models import Meal,Activity


class MealForm(ModelForm):
    class Meta():
        model = Meal
        fields = ['nameOfMeal', 'descriptionOfMeal', 'date','favourite','image']

class ActivityForm(ModelForm):
    class Meta():
        model = Activity
        fields = ['activity', 'description', 'date']