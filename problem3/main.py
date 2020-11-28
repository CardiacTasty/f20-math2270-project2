import numpy as np


PROB = {
    "room1": {
        "room1": 0,
        "room2": 0.45,
        "room3": 0.45,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 0,
        "room8": 0,
        "room9": 0,
        "trapped": 0.1,
    },
    "room2": {
        "room1": 1,
        "room2": 0,
        "room3": 0,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 0,
        "room8": 0,
        "room9": 0,
        "trapped": 0,
    },
    "room3": {
        "room1": 0.25,
        "room2": 0,
        "room3": 0,
        "room4": 0.25,
        "room5": 0.25,
        "room6": 0.25,
        "room7": 0,
        "room8": 0,
        "room9": 0,
        "trapped": 0,
    },
    "room4": {
        "room1": 0,
        "room2": 0,
        "room3": 1,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 0,
        "room8": 0,
        "room9": 0,
        "trapped": 0,
    },
    "room5": {
        "room1": 0,
        "room2": 0,
        "room3": 1,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 0,
        "room8": 0,
        "room9": 0,
        "trapped": 0,
    },
    "room6": {
        "room1": 0,
        "room2": 0,
        "room3": 0.5,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 0.5,
        "room8": 0,
        "room9": 0,
        "trapped": 0,
    },
    "room7": {
        "room1": 0,
        "room2": 0,
        "room3": 0,
        "room4": 0,
        "room5": 0,
        "room6": 0.3333,
        "room7": 0,
        "room8": 0.3333,
        "room9": 0.3334,
        "trapped": 0,
    },
    "room8": {
        "room1": 0,
        "room2": 0,
        "room3": 0,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 1,
        "room8": 0,
        "room9": 0,
        "trapped": 0,
    },
    "room9": {
        "room1": 0,
        "room2": 0,
        "room3": 0,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 1,
        "room8": 0,
        "room9": 0,
        "trapped": 0,
    },
    "trapped": {
        "room1": 0,
        "room2": 0,
        "room3": 0,
        "room4": 0,
        "room5": 0,
        "room6": 0,
        "room7": 0,
        "room8": 0,
        "room9": 0,
        "trapped": 1,
    },
}

ROOMS = list(PROB.keys())


def next_room(current):
    """
    Given the probabilities declared in PROBS, determine which room the mouse next visits.
    """

    return np.random.choice(ROOMS, p=list(PROB[current].values()))


def run_until_trapped(start):
    """
    Let the mouse run until he becomes trapped.

    Returns the sequence of rooms visited.
    """

    sequence = [start]

    current = start
    while current != "trapped":
        current = next_room(current)
        sequence.append(current)

    return sequence


print(f"{run_until_trapped('room1') = }")
