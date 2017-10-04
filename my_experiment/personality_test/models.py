from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kellogg School of Management'

doc = """
16-question personality test.
"""


class Constants(BaseConstants):
    name_in_url = 'personality_test'
    players_per_group = None
    questions = [
        "I prefer to do things the same way over and over again.",
        "Other people frequently tell me that what I've said is impolite, even though I think it is polite.",
        "In a social group, I can easily keep track of several different people's conversations.",
        "When I'm reading a story, I find it difficult to work out the characters' intentions.",
        "I don't particularly enjoy reading fiction.",
        'I find it easy to "read between the lines" when someone is talking to me',
        "I don't usually notice small changes in a situation or a person's appearance.",
        "I know how to tell if someone listening to me is getting bored.",
        "I find it easy to do more than one thing at once.",
        "When I talk on the phone, I'm not sure when it's my turn to speak.",
        "I am often the last to understand the point of a joke.",
        "I find it easy to work out what someone is thinking or feeling just by looking at their face.",
        "If there is an interruption, I can switch back to what I was doing very quickly.",
        "People often tell me that I keep going on and on about the same thing.",
        "I find it difficult to work out people's intentions.",
        "I am a good diplomat.",
    ]
    num_rounds = len(questions)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(), min=1, max=4)

    def question(self):
        return Constants.questions[self.round_number-1]
