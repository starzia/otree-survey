from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = models.Player
    form_fields = ['answer']
    # on timeout, choose a value in the middle so as not to skew the average.
    timeout_submission = {'answer':50}


class ResultsWaitPage(WaitPage):
    title_text = "Please wait"
    body_text = "Waiting for all the other participants to answer."

    def after_all_players_arrive(self):
        self.group.set_payoffs()


page_sequence = [
    Question,
    ResultsWaitPage,
]
