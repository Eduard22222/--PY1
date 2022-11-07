from pprint import pprint


def system_of_calculation(num_list: list) -> list:
    result_list = []
    for value in num_list:
        keylist_ = ['bin', 'dec', 'hex', 'oct']
        dict_value = dict.fromkeys(keylist_)
        dict_value['bin'] = bin(value)
        dict_value['dec'] = value
        dict_value['hex'] = hex(value)
        dict_value['oct'] = oct(value)
        result_list.append(dict_value)
    return result_list


test_ = range(16)
pprint(system_of_calculation(test_))
