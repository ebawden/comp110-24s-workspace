"""Mutating functions."""

__author__ = "730649327"


def manual_append(parameter_1: list[int], parameter_2: int) -> None:
    """Part 1."""
    parameter_1.append(parameter_2)


a: int = 12345
print(a)


def double(parameter_1: list[int]) -> None:
    """Part 2."""
    # parameter_1.append(1)
    index_counter: int = 0
    while index_counter < len(parameter_1):
        parameter_1[index_counter] *= 2
        index_counter += 1


b: list[int] = [1, 2, 3, 4, 5]
manual_append(b, 2)
double(b)
print(b)