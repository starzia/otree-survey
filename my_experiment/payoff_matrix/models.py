from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'payoff_matrix'
    players_per_group = None
    shapes = '■︎●▲★▬'
    choices = [
        [0,2],
        [4,1],
        [2,3],
        [1,4],
        [3,0]
    ]
    payoffs = [
        [
            [[10,10],[0,0]],
            [[0,0],[10,10]]
        ],
        [
            [[22,22],[0,7]],
            [[7,0],[10,10]]
        ],
        [
            [[22,20],[0,0]],
            [[7,0],[10,10]]
        ],
        [
            [[22,20],[0,2]],
            [[2,0],[10,10]]
        ],
        [
            [[22,20],[0,0]],
            [[0,0], [15,17]]
        ],
    ]
    num_rounds = len(payoffs)


class Subsession(BaseSubsession):
    def choices(self):
        return [Constants.shapes[i] for i in Constants.choices[self.round_number-1]]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
