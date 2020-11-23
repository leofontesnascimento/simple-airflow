#!/usr/bin/env python3

import logging
import random


def get_advice():
    # all advices quotes was extracted from:
    # https://www.goalcast.com/2017/12/12/yoda-quotes-star-wars/
    advices = [
        'Once you start down the dark path, forever will it dominate your '
        'destiny, consume you it will.',
        'Luminous beings are we, not this crude matter.',
        'In a dark place we find ourselves, and a little more knowledge '
        'lights our way.',
        'Fear is the path to the dark side. Fear leads to anger. Anger '
        'leads to hate. Hate leads to suffering.',
        'Patience you must have, my young padawan.',
        'When nine hundred years old you reach, look as good you will not.',
        'Truly wonderful, the mind of a child is.',
        'A Jedi uses the Force for knowledge and defense, never for attack.',
        'Adventure. Excitement. A Jedi craves not these things.',
        'No! Try not! Do or do not, there is no try.',
        'Judge me by my size, do you?',
        'Wars not make one great.',
        'Clear your mind must be, if you are to find the villains behind '
        'this plot.',
        'Always two there are, no more, no less. A master and an apprentice.',
        'Always pass on what you have learned.',
        'Mind what you have learned. Save you it can.',
        'To answer power with power, the Jedi way this is not.',
        'In this war, a danger there is, of losing who we are.',
        'Attachment leads to jealously. The shadow of greed, that is.',
        'In the end, cowards are those who follow the dark side.',
        'So certain were you. Go back and closer you must look.',
        'Train yourself to let go of everything you fear to lose.',
        'When you look at the dark side, careful you must be. '
        'For the dark side looks back.',
        'You will find only what you bring in.',
        'Difficult to see. Always in motion is the future...',
        'If no mistake have you made, yet losing you are... '
        'a different game you should play.',
        'Control, control, you must learn control!'
    ]

    r_index = random.randint(0, len(advices))
    advice = '"{}"'.format(advices[r_index])
    return advice


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    yoda_advice = get_advice()
    logging.info(yoda_advice)

