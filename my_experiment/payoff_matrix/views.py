from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Example(Page):
    pass


class Question(Page):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


page_sequence = [
    Instructions,
    Example,
    Question,
    ResultsWaitPage
]
