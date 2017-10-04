from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Kellogg School of Management'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'coin_toss'
    players_per_group = None
    num_rounds = 1
    payoff = [
        [1.5, 1.5],
        [1.3, 1.8],
        [1.1, 2.1],
        [.9, 2.4],
        [.7, 2.7],
        [.6, 2.8],
        [.4, 2.9],
        [0, 3]
    ]


def scaled_payoffs(factor=1):
    return [[factor * c(i) for i in j] for j in Constants.payoff]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.PositiveIntegerField(choices=range(1,9))
    coin_toss = models.IntegerField()

    def payoffs(self):
        return scaled_payoffs(factor=(2 if self.session.config["high_payment"] else 1))

    def flip_coin(self):
        self.coin_toss = random.randint(1, 2)
        self.payoff = self.payoffs()[self.answer-1][self.coin_toss-1]
        self.participant.vars["coin_payoff"] = self.payoff
        self.participant.vars["coin_payoff_possibilities"] = self.payoffs()[self.answer-1]
        self.participant.vars["coin_random_column"] = self.coin_toss
        self.participant.vars["coin_answer"] = self.answer

