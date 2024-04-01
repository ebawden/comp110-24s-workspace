"""EX05--Dictionary Utils."""

__author__ = "730649327"


def invert(parameter_1: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    dict_1: dict[str, str] = {}
    for i in parameter_1:
        value = parameter_1[i] 
        if value in dict_1:
            raise KeyError("Key already exists.")
        dict_1[value] = i
    return dict_1


def favorite_color(parameter_2: dict[str, str]) -> str:
    """Returns most frequent color in dict."""
    inverted: dict[str, str] = {}
    for key in parameter_2:
        inverted[parameter_2[key]] = key
    max: int = 0
    current: int = 0
    max_str: str = ""
    for keyi in inverted:
        for keyc in parameter_2:
            if parameter_2[keyc] == keyi:
                current += 1
                if current > max:
                    max = current
                    max_str = keyi
        current = 0
    return max_str


def count(parameter_3: list[str]) -> dict[str, int]:
    """How many times the value appeared."""
    dicti: dict[str, int] = {}
    for i in parameter_3:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    return dicti
    

def alphabetizer(parameter_4: list[str]) -> dict[str, list[str]]:
    """Puts words in alphabetical order."""
    alphad: dict[str, list[str]] = {}
    for i in parameter_4:
        if i.lower()[0] in alphad:
            alphad[i.lower()[0]].append(i)
        else:
            alphad[i.lower()[0]] = [i]
    return alphad


def update_attendance(parameter_5: dict[str, list[str]], dotw: str, student: str) -> None:
    """Mutate and return dictionary."""
    if dotw in parameter_5:
        if student not in parameter_5[dotw]:
            parameter_5[dotw].append(student)
    else:
        parameter_5[dotw] = [student]
    return None