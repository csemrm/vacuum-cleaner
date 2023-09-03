from django.urls import path
from .views import VacuumCleanerDataView

urlpatterns = [
    path('', VacuumCleanerDataView.as_view(), name='vacuum-cleaner-api'),
]
