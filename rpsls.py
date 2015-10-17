"""
rpsls.py - Rock Paper Scissors Lizard Spock module
Author: Enzo

Plays Rock, Paper, Scissors, Lizard, Spock

Winning determined by:
scissors > paper > rock > lizard > spock > scissors > lizard > paper > spock > rock > scissors
"""

import random
from sopel.module import commands

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
lizard = 'Lizard'
spock = 'Spock'
choices = rock, paper, scissors, lizard, spock

@commands('rock')
def pick_rock(bot, trigger):
    """Pick 'Rock' in a game of 'Rock Paper Scissors Lizard Spock'"""
    choice = random.choice(choices)
    bot.reply(result(choice, rock))


@commands('paper')
def pick_paper(bot, trigger):
    """Pick 'Paper' in a game of 'Rock Paper Scissors Lizard Spock'"""
    choice = random.choice(choices)
    bot.reply(result(choice, paper))


@commands('scissors')
def pick_scissors(bot, trigger):
    """Pick 'Scissors' in a game of 'Rock Paper Scissors Lizard Spock'"""
    choice = random.choice(choices)
    bot.reply(result(choice, scissors))


@commands('lizard')
def pick_lizard(bot, trigger):
    """Pick 'Lizard' in a game of 'Rock Paper Scissors Lizard Spock'"""
    choice = random.choice(choices)
    bot.reply(result(choice, lizard))


@commands('spock')
def pick_spock(bot, trigger):
    """Pick 'Spock' in a game of 'Rock Paper Scissors Lizard Spock'"""
    choice = random.choice(choices)
    bot.reply(result(choice, spock))


def result(a, b):
    return 'I picked {}! {}! {}'.format(a, fightText(a, b), winner(a, b))

def fightText(a, b):
    if (a==b):
        return 'Oops'
    elif ((a==scissors and b==paper) or (a==paper and b==scissors)):
        return 'Scissors cuts Paper'
    elif ((a==paper and b==rock) or (a==rock and b==paper)):
        return 'Paper covers Rock'
    elif ((a==rock and b==lizard) or (a==lizard and b==rock)):
        return 'Rock crushes Lizard'
    elif ((a==lizard and b==spock) or (a==spock and b==lizard)):
        return 'Lizard poisons Spock'
    elif ((a==spock and b==scissors) or (a==scissors and b==spock)):
        return 'Spock smashes Scissors'
    elif ((a==scissors and b==lizard) or (a==lizard and b==scissors)):
        return 'Scissors decapitates Lizard'
    elif ((a==lizard and b==paper) or (a==paper and b==lizard)):
        return 'Lizard eats Paper'
    elif ((a==paper and b==spock) or (a==spock and b==paper)):
        return 'Paper disproves Spock'
    elif ((a==spock and b==rock) or (a==rock and b==spock)):
        return 'Spock vaporizes Rock'
    elif ((a==rock and b==scissors) or (a==scissors and b==rock)):
        return 'Rock crushes Scissors'
    else:
        return 'uh oh'

win = 'I win! :)'
lose = 'You win! :('
tie = 'We tie.'
def winner(a, b):
    if (a==b):
        return tie
    elif (a==rock):
        return win if (b==lizard or b==scissors) else lose
    elif (a==paper):
        return win if (b==rock or b==spock) else lose
    elif (a==scissors):
        return win if (b==paper or b==lizard) else lose
    elif (a==lizard):
        return win if (b==spock or b==paper) else lose
    elif (a==spock):
        return win if (b==scissors or b==rock) else lose
