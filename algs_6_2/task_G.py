# def censored_product(quantity: int, crudity: int, string: str) -> int:
#     max_length = 0
#     string_params = []
#     index = 0
#     a_before = 0
#
#     for char in string:
#         if char == "a":
#             string_params.append({'index': index, 'letter': 'a', 'a_before': a_before})
#             a_before += 1
#             index += 1
#         elif char == "b":
#             string_params.append({'index': index, 'letter': 'b', 'a_before': a_before})
#             index += 1
#         else:
#             index += 1
#
#     if not string_params or a_before == 0:
#         return quantity
#
#     prefix_sums = {}
#     summa = 0
#     for item in string_params:
#         if item['letter'] == "b":
#             summa += item['a_before']
#             prefix_sums[item['index']] = summa
#
#     begin = 0
#     end = 0
#     prefix = 0
#     tail = 0
#     b_count = 0
#     while end < quantity:
#         if string[begin] == 'a'
#
#     return max_length


# def input_censored_product() -> None:
#     quantity, crudity = map(int, input().split())
#     string = input()
#     print(censored_product(quantity, crudity, string))
#
#
# input_censored_product()


def censored_product(quantity: int, crudity: int, string: str) -> int:
    max_length = 0
    begin = 0
    end = 0
    a_tail = 0
    cur_cru = 0
    b_count = 0

    while begin <= end < quantity:
        if string[end] == 'a':
            a_tail += 1
        if string[end] == 'b':
            cur_cru += a_tail
            b_count += 1

        print(begin, end, cur_cru, a_tail)
        if cur_cru <= crudity:
            if end - begin + 1 >= max_length:
                max_length = end - begin + 1
            end += 1
        else:
            while begin <= end and cur_cru > crudity:
                if string[begin] == 'a':
                    cur_cru -= b_count
                    a_tail -= 1
                elif string[begin] == 'b':
                    b_count -= 1
                begin += 1
                a_tail -= int(string[end] == 'a')
                if string[end] == 'b':
                    cur_cru -= a_tail
                    b_count -= 1
            if end - begin + 1 >= max_length:
                max_length = end - begin + 1

    return max_length


def input_censored_product() -> None:
    quantity, crudity = map(int, input().split())
    string = input()
    print(censored_product(quantity, crudity, string))


input_censored_product()

# aaabaababaabaaaabaabbxaazbaaaababaababbbaaaabaabbb