from urllib.parse import urlencode  # 追加

from django.shortcuts import redirect, render  # 追加
from django.urls import reverse  # 追加


def index(request):
    return render(request, "wordbook/index.html")


def register(request):
    pass


def select(request):  # 追加
    if request.method == "POST":
        mode = request.POST["mode"]
        style = request.POST["style"]
        how_many = request.POST["how_many"]

        redirect_url = reverse("wordbook:quiz")
        params = urlencode(
            {
                "mode": mode,
                "style": style,
                "how_many": how_many,
            }
        )
        url = redirect_url + "?" + params
        return redirect(url)

    return render(request, "wordbook/select.html")


def wordlist(request):
    pass


def quiz(request):
    pass


def answer(request):
    pass
