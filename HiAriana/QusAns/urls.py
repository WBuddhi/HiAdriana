from django.urls import path

from . import views

app_name = 'QusAns'
urlpatterns = [
            path('', views.index, name='index'),
            path('<int:pk>/Questionnaire/', views.qus, name='qus_ans'),
            path('<int:pk>/QAResults/', views.end, name='qa_result')
        ]
