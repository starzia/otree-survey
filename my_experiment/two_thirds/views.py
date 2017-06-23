from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import channels
import json
from otree.common_internal import channels_group_by_arrival_time_group_name as channel_name


class Question(Page):
    form_model = models.Player
    form_fields = ['answer']
    # on timeout, choose a value in the middle so as not to skew the average.
    timeout_submission = {'answer':50}

    # Before moving on, we determine if we were the last person to finish,
    # and if so then send a message to other players so they can proceed to view the results.
    # See also the TwoThirdsWaitPage view in the results app
    def before_next_page(self):
        # we get the list of those players who are already ahead of me
        already_passed = [p for p in self.player.get_others_in_subsession() if p.last_one == False]
        if len(already_passed) < len(self.player.get_others_in_subsession()):
            # this player is not the last one
            self.player.last_one = False
        else:
            # if this player is the last one in session...
            self.player.last_one = True

            # calculate payoffs
            self.group.set_payoffs()

            # we set session level var to True so other players arriving to
            # results.WaitPage later can go on immediately
            self.session.vars['two_thirds_all_done'] = True

            # send a message to other players who may be waiting on the results.TwoThirdsWaitPage
            wp_index = self.session.vars.get('two_thirds_wait_page_index')
            if wp_index:
                # for convenience, we use the "group_by_arrival_time" channel,
                # created by setting group_by_arrival_time = True in results.TwoThirdsWaitPage
                channel = channel_name(self.session.pk, wp_index)
                channels.Group(channel).send(
                    {'text': json.dumps({'status': 'ready'})}
                )


page_sequence = [
    Question
]
