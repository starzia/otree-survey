from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = models.Player

    def get_form_fields(self):
        return ['matrix_answer'] + (['social_cues_answer'] if self.player.show_social_cues() else [])

    def matrix_answer_choices(self):
        return self.player.choices()

    def social_cues_answer_choices(self):
        return self.player.social_cues()[3:5]


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


page_sequence = [
    Question, ResultsWaitPage
]
