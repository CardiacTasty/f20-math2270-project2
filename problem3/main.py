from collections import Counter, defaultdict
import numpy as np
import matplotlib.pyplot as plt


MOUSE_PROB = {
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

MOUSE_ROOMS = list(MOUSE_PROB.keys())


def next_room(current):
    """
    Given the probabilities declared in MOUSE_PROB, determine which room the mouse next visits.
    """

    return np.random.choice(MOUSE_ROOMS, p=list(MOUSE_PROB[current].values()))


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


def generate_plot(runs):
    """
    Generate a plot given some number of executions.
    """

    total = defaultdict(int)
    for _ in range(runs):
        counts = Counter(run_until_trapped("room1"))
        for room in MOUSE_ROOMS:
            total[room] += counts.get(room, 0)

    values = [total[x] for x in MOUSE_ROOMS]

    _ = plt.figure(figsize=(10, 5))
    plt.bar(MOUSE_ROOMS, values, label="Rooms")
    plt.title(f"{runs} Trials")
    plt.xlabel("Visited Rooms")
    plt.ylabel("No. of times visited")

    for i, val in enumerate(values):
        plt.text(i - 0.25, val, str(val))

    plt.savefig("genfig-3.png")


def run_single():
    """
    Produce the output for a single run through.
    """

    execution = run_until_trapped("room1")

    answer = f"""
    Problem 3:
        Rooms Before Trapped: {len(execution) - 1}
        Sequence Of Rooms: {execution}
    """

    print(answer)


run_single()
generate_plot(1000)
