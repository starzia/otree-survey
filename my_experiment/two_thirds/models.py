from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kellogg School of Management'

doc = """
Participants try to guess two-thirds of the average of all guesses.
"""


class Constants(BaseConstants):
    name_in_url = 'two_thirds'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    two_thirds = models.FloatField()

    def set_payoffs(self):
        players = self.get_players()
        average = sum([p.answer for p in players]) / len(players)
        self.two_thirds = (2.0/3) * average
        min_error = min([abs(p.answer - self.two_thirds) for p in players])
        for p in self.get_players():
            won = abs(p.answer - self.two_thirds) == min_error
            if won:
                p.payoff = p.max_payoff()
            p.participant.vars['twothirds_payoff'] = p.payoff
            p.participant.vars['twothirds_answer'] = p.answer
            p.participant.vars['twothirds_average'] = average
            p.participant.vars['twothirds_twothirds'] = self.two_thirds
            p.participant.vars['twothirds_won'] = won


class Player(BasePlayer):
    answer = models.IntegerField(min=0, max=100)

    def max_payoff(self):
        return c(10 if self.session.config["high_payment"] else 5);

