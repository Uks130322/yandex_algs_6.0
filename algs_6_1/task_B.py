def get_socks_and_shirts(blue_shirt: int, red_shirt: int, blue_sock: int, red_sock: int) -> tuple[int]:
    if blue_shirt == red_shirt:
        return blue_shirt + 1, 1
    if blue_sock == red_sock:
        return 1, red_shirt + 1
    if blue_shirt == 0:
        return 1, blue_sock + 1
    if red_shirt == 0:
        return 1, red_sock + 1
    if blue_sock == 0:
        return blue_shirt + 1, 1
    if red_sock == 0:
        return red_shirt + 1, 1

    one_blue_shirt = red_shirt + 1
    one_blue_sock = red_sock + 1
    one_red_shirt = blue_shirt + 1
    one_red_sock = blue_sock + 1

    blue_pair = (one_blue_shirt, one_blue_sock)
    red_pair = (one_red_shirt, one_red_sock)
    all_color_shirt = (max(blue_shirt, red_shirt) + 1, 1)
    all_color_socks = (1, max(blue_sock, red_sock) + 1)

    result = ([blue_pair, red_pair, all_color_shirt, all_color_socks])
    result.sort(key=lambda item: sum(item))
    return result[0]


def input_get_socks_and_shirts() -> None:
    blue_shirt = int(input())
    red_shirt = int(input())
    blue_sock = int(input())
    red_sock = int(input())
    print(*get_socks_and_shirts(blue_shirt, red_shirt, blue_sock, red_sock))

# input_get_socks_and_shirts()