# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_imperative(lst: list[int | float]) -> list[int | float]:
    temp: int | float
    for j in range(0, len(lst) - 1):
        temp = lst[j]
        temp_ind = j
        for i in range(j, len(lst)):
            if lst[i] > temp:
                temp_ind = i
                temp = lst[i]
        lst[temp_ind] = lst[j]
        lst[j] = temp
    print(lst)
    return lst


def sort_list_declarative(lst: list[int | float]) -> list[int | float]:
    return sorted(lst, reverse=True)


sort_list_imperative([12.5, -7, 89, 0, 12, 17, 750])
print("*****")
print(sort_list_declarative([12.5, -7, 89, 0, 750, 17, 12]))


