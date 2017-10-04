from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class TwoThirdsWaitPage(WaitPage):
    title_text = "Please wait"
    body_text = "Waiting for all the other participants to submit a guess for the 2/3 game."

    # below is a hack to create a channel that we can use to signal completion of the 2/3 game
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        # this variable is used by the Question view in the two_thirds app
        self.session.vars['two_thirds_wait_page_index'] = self._index_in_pages

        # if all players have finished the two_thirds game then we proceed, otherwise just wait
        if self.session.vars.get('two_thirds_all_done'):
            return waiting_players


class Results(Page):
    pass


page_sequence = [
    TwoThirdsWaitPage,
    Results
]
