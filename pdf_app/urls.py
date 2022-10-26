# todo/todo_api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
from .views import (
    CreatePDFReportView,CreateMethodTestView
)

urlpatterns = [
    path('report-lab/', CreatePDFReportView.as_view()),
    path('post-method-test/', CreateMethodTestView.as_view()),
]