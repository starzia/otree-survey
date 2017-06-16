from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from payoff_matrix.models import image_for_shape


author = 'Kellogg School of Management'

doc = """
Overall instructions and instructions for the Payoff Matrix game.
"""


class Constants(BaseConstants):
    name_in_url = 'instructions1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def social_cues(self):
        return self.session.config["social_cues"]

    def payment(self):
        return 35 if self.session.config["high_payment"] else 20;

    def shape(self):
        return [image_for_shape(i) for i in [0, 1]]