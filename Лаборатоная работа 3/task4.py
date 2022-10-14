salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
month = 0
while month < 10:
    a = salary - spend
    spend *= (1 + increase)
    need_money += - a
    month += 1
print(round(need_money))

