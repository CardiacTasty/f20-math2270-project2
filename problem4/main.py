from collections import Counter, defaultdict
import numpy as np
import matplotlib.pyplot as plt


WEATHER_PROB = {
    "sunny": {
        "sunny": 6 / 7,
        "partcloudy": 1 / 7,
        "cloudy": 0,
        "snowing": 0,
    },
    "partcloudy": {
        "sunny": 1 / 3,
        "partcloudy": 1 / 3,
        "cloudy": 1 / 3,
        "snowing": 0,
    },
    "cloudy": {
        "sunny": 1 / 3,
        "partcloudy": 0,
        "cloudy": 1 / 3,
        "snowing": 1 / 3,
    },
    "snowing": {
        "sunny": 0,
        "partcloudy": 0,
        "cloudy": 1,
        "snowing": 0,
    },
}

WEATHER_PAT = list(WEATHER_PROB.keys())


def next_pattern(current):
    """
    Given the probabilities declared in WEATHER_PAT, determine which room the mouse next visits.
    """

    return np.random.choice(WEATHER_PAT, p=list(WEATHER_PROB[current].values()))


def run_from_start(start, transitions=30):
    """
    Let the weather shift for the number of transitions.

    Returns the sequence of weather patterns.
    """

    sequence = [start]

    current = start
    for _ in range(transitions):
        current = next_pattern(current)
        sequence.append(current)

    return sequence


def generate_plot(runs):
    """
    Generate a plot given some number of executions.
    """

    total = defaultdict(int)
    for _ in range(runs):
        counts = Counter(run_from_start("sunny"))
        for pattern in WEATHER_PAT:
            total[pattern] += counts.get(pattern, 0)

    values = [total[x] for x in WEATHER_PAT]

    _ = plt.figure(figsize=(10, 5))
    plt.bar(WEATHER_PAT, values, label="patterns")
    plt.title(f"{runs} Trials")
    plt.xlabel("Visited patterns")
    plt.ylabel("No. of times visited")

    for i, val in enumerate(values):
        plt.text(i - 0.25, val, str(val))

    plt.savefig("genfig-4.png")


def output_single():
    """
    Produce the output for a single run through.
    """

    execution = run_from_start("sunny")

    answer = f"""
    Problem 4:
        Sequence Of Weather Patterns: {execution}
    """

    print(answer)


output_single()
generate_plot(1000)
