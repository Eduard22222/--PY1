list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = list_numbers[0]
for current in list_numbers:
    if current > max_i:
        max_i= current

a = list_numbers.index(max_i)
list_numbers[a], list_numbers[-1] = list_numbers[-1], list_numbers[a]

print(list_numbers)

