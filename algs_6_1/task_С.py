def read_the_letter(scoreboard: list[str]) -> str:
    scoreboard = vertical_smash(scoreboard)
    if scoreboard == "X":
        return "X"
    scoreboard = horisontal_smash(scoreboard)
    if scoreboard == "X":
        return "X"
    if len(scoreboard[0]) > 3 or len(scoreboard) > 4:
        return "X"
    elif scoreboard == ["#"]:
        return "I"
    elif scoreboard == ["#.",
                        "##"]:
        return "L"
    elif scoreboard == ["##",
                        "#.",
                        "##"]:
        return "C"
    elif scoreboard == ["###",
                        "#.#",
                        "###"]:
        return "O"
    elif scoreboard == ["#.#",
                        "###",
                        "#.#"]:
        return "H"
    elif scoreboard == ["###",
                        "#.#",
                        "###",
                        "#.."]:
        return "P"
    else:
        return "X"


def vertical_smash(scoreboard: list[str]) -> list[str]:
    new_scoreboard = []
    last = "0"
    first_time = True
    for string in scoreboard:
        if "#" not in string:
            if last != "0":
                first_time = False
        elif first_time:
            if string != last:
                new_scoreboard.append(string)
                last = string
        else:
            return "X"
    return new_scoreboard


def horisontal_smash(scoreboard: list[str]) -> list[str]:
    turned_scoreboard = ["".join([string[index] for string in scoreboard]) for index in range(len(scoreboard[0]))]
    new_scoreboard = vertical_smash(turned_scoreboard)
    if new_scoreboard == "X":
        return "X"
    final_scoredboard = ["".join([string[index] for string in new_scoreboard])
                         for index in range(len(new_scoreboard[0]))]
    return final_scoredboard


def input_read_the_letter() -> None:
    n = int(input())
    scoreboard = []
    for i in range(n):
        scoreboard.append(input())
    print(read_the_letter(scoreboard))


input_read_the_letter()

# print(read_the_letter([".###.",
#                        ".#.#.",
#                        ".###.",
#                        ".#...",
#                        "....."]))
