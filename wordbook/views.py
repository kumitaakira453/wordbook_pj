from urllib.parse import urlencode  # 追加

from django.shortcuts import redirect, render  # 追加
from django.urls import reverse  # 追加

from .models import Word


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
    context = {
        "words": Word.objects.all(),
    }
    return render(request, "wordbook/wordlist.html", context)


# 省略


def quiz(request):  # 追加
    mode = request.GET["mode"]
    style = request.GET["style"]

    try:
        how_many = int(request.GET["how_many"])
    except ValueError:
        how_many = 0
        print("ValueError発生")

    all_words = Word.objects.all()

    all_word_counts = all_words.count()
    if how_many > all_word_counts:
        how_many = all_word_counts

    if request.method == "GET":
        words = all_words.order_by("?")[:how_many]

        context = {
            "mode": mode,
            "style": style,
            "how_many": how_many,
            "words": words,
        }

    elif request.method == "POST":
        info = {
            "mode": mode,
            "style": style,
            "how_many": how_many,
        }

        word_ids = dict()
        answers = dict()
        if mode == "en_to_ja":
            for i in range(1, how_many + 1):
                try:
                    answer = request.POST["question_" + str(i)]
                    answers["answer" + str(i)] = answer
                    word_id = int(request.POST["word_" + str(i)])
                    word_ids["word_id" + str(i)] = word_id
                    word = all_words.get(pk=word_id)
                    if answer == word.ja_word:
                        word.en_to_ja_correct_count += 1
                        word.save()
                    else:
                        word.en_to_ja_incorrect_count += 1
                        word.save()
                except ValueError:
                    print("ValueError発生")
        else:
            for i in range(1, how_many + 1):
                try:
                    answer = request.POST["question_" + str(i)]
                    answers["answer" + str(i)] = answer
                    word_id = int(request.POST["word_" + str(i)])
                    word_ids["word_id" + str(i)] = word_id
                    word = all_words.get(pk=word_id)
                    if answer == word.en_word:
                        word.ja_to_en_correct_count += 1
                        word.save()
                    else:
                        word.ja_to_en_incorrect_count += 1
                        word.save()
                except ValueError:
                    print("ValueError発生")

        redirect_url = reverse("wordbook:answer")
        params = urlencode(dict(info | word_ids | answers))
        url = str(redirect_url) + "?" + str(params)
        return redirect(url)

    return render(request, "wordbook/quiz.html", context)


def answer(request):
    pass
