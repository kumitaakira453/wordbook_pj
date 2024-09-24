from django.urls import path

from . import views

app_name = "wordbook"

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("select", views.select, name="select"),
    path("wordlist", views.wordlist, name="wordlist"),
    path("quiz", views.quiz, name="quiz"),
    path("answer", views.answer, name="answer"),
]
