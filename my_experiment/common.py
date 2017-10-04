from random import sample, shuffle

def group_players_and_set_money_round(subsession, num_rounds):
    # group players
    if subsession.round_number == 1:
        shuffled_players = subsession.get_players()
        shuffle(shuffled_players)
        list_of_lists = []
        for i, p in enumerate(shuffled_players):
            # the last player has to be in a group of three if he's the odd man out
            if i == len(shuffled_players) - 1 and i % 2 == 0:
                list_of_lists[-1].append(p)
            # everyone else
            elif i % 2 == 0:
                # start a new group
                list_of_lists.append([p])
            else:
                # add to prior group
                list_of_lists[-1].append(p)
        subsession.set_group_matrix(list_of_lists)
    else:
        subsession.group_like_round(1)

    # choose money round for each group
    for g in subsession.get_groups():
        if subsession.round_number == 1:
            g.money_round = 1 + sample(range(num_rounds), 1)[0]
        else:
            g.money_round = g.in_round(1).money_round
