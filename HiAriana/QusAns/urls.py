from django.urls import path

from . import views

app_name = 'QusAns'
urlpatterns = [
            path('', views.index, name='index'),
            path('Questionnaire/', views.qus, name='qus_ans')
        ]
