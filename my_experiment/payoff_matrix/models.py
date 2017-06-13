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
    descriptions = [
        ("If you both choose the same symbol, you each get $%d. If you choose different symbols, you each get $0.",
         [[0, 0, 0]]),  # index of payoff
        ("If you both choose %s, you each get $%d. If you both choose %s, you each get $%d. "
         + "If you choose %s and the other participant chooses %s, you get $0 and the other participant $%d. "
         + "If you choose %s and the other participant chooses %s, you get $%d and the other participant $0.",
         [0, [0, 0, 0], 1, [1, 1, 0], 0, 1, [0, 1, 1], 1, 0, [1, 0, 0]]),
        ("If you both choose %s, you get $%d and the other participant gets $%d. "
         + "If you both choose %s, then you get $%d and the other participant gets $%d. "
         + "If you choose different symbols, you each get $0.",
         [0, [0, 0, 0], [0, 0, 1], 1, [1, 1, 0], [1, 1, 1]]),
        ("If you both choose %s, you each get $%d. "
         + "If you both choose %s, you each get $%d. "
         + "If you choose %s and the other participant chooses %s, you get $%d and the other participant $%d. "
         + "If you choose %s and the other participant chooses %s, you get $%d and the other participant $%d. ",
         [0, [0, 0, 0],
          1, [1, 1, 0],
          0, 1, [0, 1, 0], [0, 1, 1],
          1, 0, [1, 0, 0], [1, 0, 1]]),
        ("If you both choose %s, you get $%d and the other participant gets $%d. "
         + "If you both choose %s, then you get $%d and the other participant gets $%d. "
         + "If you choose different symbols, you each get $0.",
         [0, [0, 0, 0], [0, 0, 1], 1, [1, 1, 0], [1, 1, 1]]),
    ]
    num_rounds = len(payoffs)


def double_payoffs(payoffs):
    return [[[2*i for i in j] for j in k] for k in payoffs]


def column_payoffs(payoffs):
    transposed = [[payoffs[0][0], payoffs[1][0]], [payoffs[0][1], payoffs[1][1]]]
    return [[list(reversed(j)) for j in i] for i in transposed]


class Subsession(BaseSubsession):
    def before_session_starts(self):
        # group players
        if self.round_number == 1:
            shuffled_players = sample(self.get_players(), len(self.get_players()))
            list_of_lists = []
            for i, p in enumerate(shuffled_players):
                # the last player has to be in a group of three if he's the odd man out
                if i == len(shuffled_players) - 1 and i % 2 == 0:
                    list_of_lists[-1].append(p)
                # everyone else
                elif i % 2 == 0:
                    # start a new group
                    list_of_lists.append([p])
                else:
                    # add to prior group
                    list_of_lists[-1].append(p)
            self.set_group_matrix(list_of_lists)
        else:
            self.group_like_round(1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    matrix_answer = models.CharField(widget=widgets.RadioSelectHorizontal())
    social_cues_answer = models.CharField(widget=widgets.RadioSelectHorizontal())

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

    def social_cues_question(self):
        return "Is this a %s or a %s?" % tuple(self.social_cues()[1:3])

    def role(self):
        return "row" if self.id_in_group == 1 else "column"

    def description(self):
        payoffs = self.payoffs()
        (format_string, substitutions) = Constants.descriptions[self.round_number-1]
        dereferenced = []
        for i, s in enumerate(substitutions):
            # dereference payoff
            if isinstance(s, list):
                dereferenced.append(payoffs[s[0]][s[1]][s[2]])
            else:  # dereference shapes
                dereferenced.append(self.choices()[s])
        return format_string % tuple(dereferenced)
