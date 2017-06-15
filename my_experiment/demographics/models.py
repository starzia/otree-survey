from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.CharField(
        widget=widgets.RadioSelect(),
        choices=["Male", "Female", "Other"],
        verbose_name="With which gender do you most closely identify?"
    )
    age = models.PositiveIntegerField(verbose_name="How old are you?")
