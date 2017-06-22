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
    timeout_submission = {'answer': 1}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


page_sequence = [
    Instructions,
    Question,
    ResultsWaitPage
]
