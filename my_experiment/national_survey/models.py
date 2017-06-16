from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kellogg School of Management'

doc = """
Participants agree or disagree with six survey question results using a 7-point Likert scale response.
"""


class Constants(BaseConstants):
    name_in_url = 'national_survey'
    players_per_group = None
    questions = [
        [
            "Do you think the space station has been a good investment for this country, or don't you think so?",
            "Good investment (64%)", "Not a good investment (29%)"
        ],
        [
            "Do you have a favorable or unfavorable opinion of Bill Cosby?",
            "Unfavorable (61%)", "Favorable (22%)"
        ],
        [
            "Do you generally like it or dislike it if people get you socks as a gift?",
            "Dislike (20%)", "Like (56%)"
        ],
        [
            "Which of the following kills one woman every minute each day around the world?",
            "Childbirth (15%)", "Heart Attack (54%)"
        ],
        [
            "Which of the following world empires came into existence first?",
            "Roman (64%)", "Ottoman (21%)"
        ],
        [
            "Is the following statement true or false?: Plastic is made from oil.",
            "True (28%)", "False or unknown (72%)"
        ],
    ]
    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.CharField()

    def question(self):
        return self.session.vars['questions'][self.round_number - 1]

    def choices(self):
        return [{
                    "id": i,
                    "label": ["Definitely Option A", "Probably A", "Maybe A", "Unsure",
                              "Maybe B", "Probably B", "Definitely Option B"][i-1]
                } for i in range(1,8)]
