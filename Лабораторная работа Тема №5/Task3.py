from random import randrange
def get_unique_list_numbers(start=-10, end=10, size=15) -> list[int]:
    res_list = []
    while len(res_list) < size:
        res = randrange(start, end + 1)
        if res not in res_list:
            res_list.append(res)
    return res_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
