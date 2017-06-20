from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from payoff_matrix.models import image_for_shape


author = 'Kellogg School of Management'

doc = """
Part 3 instructions.
"""


class Constants(BaseConstants):
    name_in_url = 'instructions3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass