from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kellogg School of Management'

doc = """
A five-question IQ test.
"""


class Constants(BaseConstants):
    name_in_url = 'iq_test'
    players_per_group = None
    num_rounds = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.PositiveIntegerField(
        widget=widgets.Select(),
        choices=range(1,9),
        verbose_name="Select the option that best fits in the array above."
    )
