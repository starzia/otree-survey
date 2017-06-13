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
    shapes = ['■︎','●','▲','★','▬']
    shape_names = ['square', 'circle', 'triangle', 'star', 'rectangle']
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
    social_cues = [
        [2, 3],
        [1, 2],
        [3, 1],
        [4, 3],
        [0, 2]
    ]
    num_rounds = len(payoffs)


def double_payoffs(payoffs):
    return [[[2*i for i in j] for j in k] for k in payoffs]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def choices(self):
        return [Constants.shapes[i] for i in Constants.choices[self.round_number-1]]

    def payoffs(self):
        payoffs = Constants.payoffs[self.round_number-1]
        return double_payoffs(payoffs) if self.session.config["high_payment"] else payoffs

    def show_social_cues(self):
        return self.session.config["social_cues"]

    def social_cues(self):
        cues = Constants.social_cues[self.round_number-1]
        return [
            Constants.shapes[cues[0]],
            Constants.shape_names[cues[0]],
            Constants.shape_names[cues[1]],
            Constants.shapes[cues[0]],
            Constants.shapes[cues[1]]
        ]
