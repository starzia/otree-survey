from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from common import group_players_and_set_money_round


author = 'Kellogg School of Management'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'decider_receiver'
    players_per_group = None
    payoffs = [
        [
            [10, 5],
            [9.4, 5.8],
            [8.8, 6.3],
            [8.1, 6.9],
            [7.5, 7.5],
            [6.9, 8.1],
            [6.3, 8.8],
            [5.8, 9.4],
            [5, 10],
        ],
        [
            [8.5, 1.5],
            [8.7, 1.9],
            [8.9, 2.4],
            [9.1, 2.8],
            [9.3, 3.3],
            [9.4, 3.7],
            [9.6, 4.1],
            [9.8, 4.6],
            [10, 5]
        ],
        [
            [5, 10],
            [5.4, 9.8],
            [5.9, 9.6],
            [6.3, 9.4],
            [6.8, 9.3],
            [7.2, 9.1],
            [7.6, 8.9],
            [8.1, 8.7],
            [8.5, 8.5]
        ],
        [
            [5, 10],
            [5.4, 8.9],
            [5.9, 7.9],
            [6.3, 6.8],
            [6.8, 5.8],
            [7.2, 4.7],
            [7.6, 3.6],
            [8.1, 2.8],
            [8.5, 1.5]
        ],
        [
            [8.5, 8.5],
            [8.5, 7.6],
            [8.5, 6.8],
            [8.5, 5.9],
            [8.5, 5.0],
            [8.5, 4.1],
            [8.5, 3.3],
            [8.5, 2.4],
            [8.5, 1.5]
        ],
        [
            [10, 5],
            [9.8, 5.4],
            [9.6, 5.9],
            [9.4, 6.3],
            [9.3, 6.8],
            [9.1, 7.2],
            [8.9, 7.6],
            [8.7, 8.1],
            [8.5, 8.5]
        ]
    ]
    num_rounds = len(payoffs)


def scaled_payoffs(factor=1):
    return [[[factor * c(i) for i in j] for j in k] for k in Constants.payoffs]


class Subsession(BaseSubsession):
    def before_session_starts(self):
        group_players_and_set_money_round(self, Constants.num_rounds)


class Group(BaseGroup):
    money_round = models.PositiveIntegerField(doc="The round that pays out.")

    def set_payoffs(self):
        for p in self.get_players():
            opponent = self.get_player_by_role("decider" if p.role() == "receiver" else "receiver")
            try:
                p.theoretical_payoff = c(p.payoffs()
                                         [(p.answer if p.role() == "decider" else opponent.answer)-1]
                                         [0 if p.role() == "decider" else 1])
            except ValueError:
                # if we "Advanced slowest user" then choices will be missing, so there is no payout
                p.theoretical_payoff = 0
            if self.money_round == self.round_number:
                p.payoff = p.theoretical_payoff
                p.participant.vars['decider_payoff'] = p.payoff
                p.participant.vars['decider_money_round'] = self.money_round
                p.participant.vars['decider_choices'] = p.payoffs()
                p.participant.vars['decider_role'] = p.role()
                p.participant.vars['decider_decider_answer'] = (p.answer if p.role() == "decider" else opponent.answer)


class Player(BasePlayer):
    answer = models.PositiveIntegerField(choices=range(1,10))
    theoretical_payoff = models.CurrencyField(doc="Amount to be paid if this round were a money round.")

    def payoffs(self):
        return scaled_payoffs(factor=(2 if self.session.config["high_payment"] else 1))[self.round_number-1]

    def role(self):
        return "decider" if self.id_in_group == 1 else "receiver"

