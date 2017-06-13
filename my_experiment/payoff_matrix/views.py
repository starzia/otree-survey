from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = models.Player
    form_fields = ['matrix_answer', 'social_cues_answer']

    def matrix_answer_choices(self):
        return self.player.choices()

    def social_cues_answer_choices(self):
        return self.player.social_cues()[3:5]

page_sequence = [
    Question
]
