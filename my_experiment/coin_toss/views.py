from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Question(Page):
    form_model = models.Player
    form_fields = ['answer']
    timeout_submission = {'answer': 1}

    def before_next_page(self):
        self.player.flip_coin()


page_sequence = [
    Question
]
