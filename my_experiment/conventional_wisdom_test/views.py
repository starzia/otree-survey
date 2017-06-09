from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = models.Player
    form_fields = ['submitted_answer']

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        return [
            qd['a'][0],
            qd['a'][1]
        ]


class Results(Page):
    pass


page_sequence = [
    Question,
    Results
]
