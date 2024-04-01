"""EX04-List Utils."""

__author__ = "730649327"


def all(int_list: list[int], check_int: int) -> bool:
    """Determine whether all ints in list are same as given int."""
    if len(int_list) == 0:
        return False
    index_counter: int = 0
    while index_counter <= len(int_list) - 1:
        if int_list[index_counter] != check_int:
            return False
        index_counter += 1
    return True

   
def max(max_input: list[int]) -> int:
    """Determine and return the largest # in list."""
    if len(max_input) == 0:
        raise ValueError("max() arg is an empty List")
    max_number: int = max_input[0]
    index_counter: int = 0
    while index_counter <= len(max_input) - 1:
        if max_input[index_counter] > max_number:
            max_number = max_input[index_counter]
        index_counter += 1
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determine if every element in each index is equal in both of the lists."""
    if len(list_1) != len(list_2):
        return False
    index_counter: int = 0
    while index_counter <= len(list_1) - 1:
        if list_1[index_counter] != list_2[index_counter]:
            return False
        index_counter += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Mutate list_1."""
    index_counter: int = 0
    while index_counter <= len(list_2) - 1:
        list_1.append(list_2[index_counter])
        index_counter += 1