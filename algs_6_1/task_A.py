def find_nearest_side(x1: int, y1: int, x2: int, y2: int, x: int, y: int) -> str:
    if x <= x1:
        if y >= y2:
            return "NW"
        elif y > y1:
            return "W"
        else:
            return "SW"
    elif x < x2:
        if y > y2:
            return "N"
        else:
            return "S"
    else:
        if y >= y2:
            return "NE"
        elif y > y1:
            return "E"
        else:
            return "SE"


def input_find_nearest_side() -> None:
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    x = int(input())
    y = int(input())
    print(find_nearest_side(x1, y1, x2, y2, x, y))

input_find_nearest_side()