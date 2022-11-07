import string
from random import sample


def get_random_password(count_sym=8) -> str:
    symbol = string.digits + string.ascii_lowercase + string.ascii_uppercase
    password = sample(symbol, count_sym )
    password = ''.join(password)
    return password


print(get_random_password())
