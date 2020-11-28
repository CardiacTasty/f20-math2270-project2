# f20-math2270-project2

The code implementing problems #1-4 for the topic Markov Chains within Project 2.

Currently #3 is finished.

## Requirements

Be sure you have python 3 installed. Once you have python 3, install pipenv.

This project was initially developed on a linux machine; if we have the time we might get it working on Windows, and it should already work on Mac.

## Running The App

The easiest is to use the included Makefile. Failing that, running directly with pipenv can work.

### Make

To preform initial setup of the project, execute:

```bash
make init
```

To run each problem, execute:

```bash
make runall
```

### Pipenv Directly

To preform initial venv setup, execute:

```bash
pipenv install --dev
```

To run each problem, sequentially run:

```bash
pipenv run python ./problem3/main.py
```
