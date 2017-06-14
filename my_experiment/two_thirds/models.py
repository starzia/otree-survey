from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
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
        self.two_thirds = (2.0/3) * sum([p.answer for p in self.get_players()])
        min_error = min([abs(p.answer - self.two_thirds) for p in self.get_players()])
        for p in self.get_players():
            if abs(p.answer - self.two_thirds) == min_error:
                p.payoff = p.max_payoff()


class Player(BasePlayer):
    answer = models.IntegerField(min=0, max=100)

    def max_payoff(self):
        return c(10 if self.session.config["high_payment"] else 5);

