from django.db import models

# Create your models here.


class Word(models.Model):
    en_word = models.CharField(max_length=50)
    ja_word = models.CharField(max_length=50)
    en_to_ja_correct_count = models.PositiveIntegerField(default=0)
    en_to_ja_incorrect_count = models.PositiveIntegerField(default=0)
    ja_to_en_correct_count = models.PositiveIntegerField(default=0)
    ja_to_en_incorrect_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.en_word
