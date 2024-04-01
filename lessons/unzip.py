"""Splitting a dictionary into two lists."""

__author__ = "730649327"


def get_keys(parameter_1: dict[str, int]) -> list[str]:
    """Part 1."""
    list_1: list[str] = []
    if len(parameter_1) == 0:
        return list_1
    for key in parameter_1:
        if parameter_1[key]:
            list_1.append(key)
    return list_1 
 

def get_values(parameter_2: dict[str, int]) -> list[int]:
    """Part 2."""
    list_2: list[int] = []
    if len(parameter_2) == 0:
        return list_2
    for key in parameter_2:
        if parameter_2[key]:
            list_2.append(parameter_2[key])
    return list_2