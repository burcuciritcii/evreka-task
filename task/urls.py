from django.urls import path
from task.views import *

urlpatterns = [
    path('collection_frequency', collection_frequency, name='collection_frequency'),
    path('navigation_record', navigation_record, name='navigation_record'),
]