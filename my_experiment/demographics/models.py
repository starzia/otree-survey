from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kellogg School of Management'

doc = """
Gender and age question.
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
    education = models.CharField(
        widget=widgets.RadioSelect(),
        choices=["Less than high school",
                 "High school graduate (includes equivalency)",
                 "Some college, no degree",
                 "Associate's degree",
                 "Bachelor's degree",
                 "Ph.D.",
                 "Graduate or professional degree"],
        verbose_name="What is the highest degree or level of education you have completed?"
    )