def get_count_char(str_):
    DEFAULT_COUNT = 0
    dict_word = {}
    word_list = str_.split(" ")
    str_mod = "".join(word_list)
    clear_list = []
    if not str_mod.isalpha():
        for sym in list(str_mod):
            if str(sym).isalpha():
                clear_list.append(sym)
    clear_str = "".join(clear_list).lower()
    LIST_ = list(clear_str) #Создал список символов для дальнейшего подсчета количества
    clear_list = list(clear_str)
    clear_list.sort()
    for sym in clear_list:
        dict_word.setdefault(sym, DEFAULT_COUNT)   # Создал словарь с ключами в виде уникальных символов. У каждого ключа значение 0
    for sym in LIST_:
       dict_word[sym] = dict_word.get(sym, DEFAULT_COUNT) + 1 #Считаю количество каждого символа и записываю под нужным ключем в конечный словарь
    return dict_word


def percent(str_):
    DEFAULT_COUNT = 0
    dict_new = {}
    sum_ = sum(get_count_char(str_).values()) # Здесь функция get_count_char вызывается для подсчета общего количества символов
    for key, value in get_count_char(str_).items():
        persent_ = (value / sum_) * 100
        dict_new.setdefault(key, DEFAULT_COUNT)
        dict_new[key] = dict_new.get(key, DEFAULT_COUNT) + persent_
    return dict_new


main_str = """
    Данное предложение будет разбиваться на отдельные слова.
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str), type(get_count_char(main_str)))

print(percent(main_str))
