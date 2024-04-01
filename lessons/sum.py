"""Summing the elements of a list by using different loops."""

__author__ = "730649327"


def w_sum(vals: list[float]) -> float:
    """Part 1."""
    sum: float = 0.0
    index_counter: int = 0
    while index_counter < len(vals):
        sum += vals[index_counter]
        index_counter += 1
    return (sum)


def f_sum(vals: list[float]) -> float:
    """Part 2."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return (sum) 
    

def f_range_sum(vals: list[float]) -> float:
    """Part 3."""
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum += vals[elem]
    return (sum)