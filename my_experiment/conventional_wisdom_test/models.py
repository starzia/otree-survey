from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kellogg School of Management'

doc = """
A quiz app for binary-choice questions with a 7-point Likery scale response.
"""


class Constants(BaseConstants):
    name_in_url = 'conventional_wisdom_test'
    players_per_group = None
    questions = [
        {
            "id": 1,
            "question": "Do you think the space station has been a good investment for this country, or don't you think so?",
            "a": ["Good investment (64%)", "Not a good investment (29%)"]
        },
        {
            "id": 2,
            "question": "Do you have a favorable or unfavorable opinion of Bill Cosby?",
            "a": ["Unfavorable (61%)", "Favorable (22%)"]
        }
    ]
    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.PositiveIntegerField()
    question = models.CharField()
    solution = models.CharField()
    submitted_answer = models.CharField(widget=widgets.RadioSelect())
    is_correct = models.BooleanField()

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]
