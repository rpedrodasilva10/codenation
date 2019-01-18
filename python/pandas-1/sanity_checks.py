import pandas as pd

def part_0(x):
    return (
        (isinstance(x, pd.DataFrame)) and
        (x.shape == (0, 0))
    )


def part_1(x):
    return (
        isinstance(x, int)
    )


def part_2(x):
    return isinstance(x, int)


def part_3(x):
    return (
        isinstance(x, pd.Series) and
        (x.shape == (20,))
    )


def part_4(x):
    return (
        isinstance(x, pd.Series) and
        (x.shape == (10,))
    )


def part_5(x):
    return (
        isinstance(x, pd.Series) and
        (x.shape == (10,))
    )


def part_6(x):
    return isinstance(x, pd.Series)


def part_7(x):
    return isinstance(x, pd.Series)
