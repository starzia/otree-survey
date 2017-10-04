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
    num_winners = models.PositiveIntegerField()

    def set_payoffs(self):
        players = self.get_players()
        average = sum([p.answer for p in players]) / len(players)
        self.two_thirds = (2.0/3) * average
        min_error = min([abs(p.answer - self.two_thirds) for p in players])
        winners = [p for p in self.get_players() if abs(p.answer - self.two_thirds) == min_error]
        self.num_winners = len(winners)
        for p in self.get_players():
            if p in winners:
                p.payoff = p.max_payoff() / self.num_winners
            p.participant.vars['twothirds_payoff'] = p.payoff
            p.participant.vars['twothirds_answer'] = p.answer
            p.participant.vars['twothirds_average'] = average
            p.participant.vars['twothirds_twothirds'] = self.two_thirds
            p.participant.vars['twothirds_num_winners'] = self.num_winners
            p.participant.vars['twothirds_won'] = p in winners


class Player(BasePlayer):
    answer = models.IntegerField(min=0, max=100)

    # last_one is used to facilitate the WaitPage in the results app.  Remember, that it defaults to None
    last_one = models.BooleanField()

    def max_payoff(self):
        return c(10 if self.session.config["high_payment"] else 5);

