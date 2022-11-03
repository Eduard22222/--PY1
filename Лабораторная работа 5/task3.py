from random import randint


def get_unique_list_numbers() -> list[int]:
    list_random = []
    while len(set(list_random)) != 15:
        list_random.append(randint(-10, 10))
    return set(list_random)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
