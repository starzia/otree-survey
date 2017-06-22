from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    """only show instructions once"""
    def is_displayed(self):
        return self.round_number == 1


class Question(Page):
    form_model = models.Player
    form_fields = ['answer']


page_sequence = [
    Instructions, Question
]
