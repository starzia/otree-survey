from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from random import sample


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
            [[0,0],[20,22]]
        ],
        [
            [[22,22],[0,2]],
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


def column_payoffs(payoffs):
    transposed = [[payoffs[0][0], payoffs[1][0]], [payoffs[0][1], payoffs[1][1]]]
    return [[list(reversed(j)) for j in i] for i in transposed]


class Subsession(BaseSubsession):
    def before_session_starts(self):
        # match players
        if self.round_number == 1:
            shuffled_players = sample(self.get_players(), len(self.get_players()))
            for i, p in enumerate(shuffled_players):
                # the last player has to be double-matched if he's the odd man out
                partner_loc = (i-1) if i == len(shuffled_players) - 1 and i % 2 == 0 \
                                    else (i-1 if i % 2 else i+1)  # most players pair-up cleanly
                p.participant.vars['partner'] = shuffled_players[partner_loc].id_in_group
                p.participant.vars['is_row'] = (i % 2 == 0)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_row = models.BooleanField()
    partner = models.IntegerField()

    def choices(self):
        return [Constants.shapes[i] for i in Constants.choices[self.round_number-1]]

    def payoffs(self):
        payoffs = Constants.payoffs[self.round_number-1]
        payoffs = double_payoffs(payoffs) if self.session.config["high_payment"] else payoffs
        return column_payoffs(payoffs) if self.role() == "column" else payoffs

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

    def role(self):
        return "row" if self.participant.vars["is_row"] else "column"
