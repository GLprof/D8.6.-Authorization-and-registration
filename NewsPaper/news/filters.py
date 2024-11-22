import django_filters
from django.forms import DateInput
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post

class PostFilter(FilterSet):
    datetime_p = DateTimeFilter(field_name='datetime_p', lookup_expr='lt',
                                label='Позже указываемой даты',
                                widget=DateInput(
                                attrs={'placeholder': 'Select a date', 'type': 'date'}),
                                )

    class Meta:
        model = Post
        fields = {
            'post_title': ['icontains'],
            'post_author': ['exact'],

        }
