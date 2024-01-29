# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
# Можете использовать любую парадигму, но рекомендую использовать функциональную,
# т.к. в этом примере она значительно упростит вам жизнь.
#

import math

def pearson_correlation(x: list[int], y: list[int]) -> float | None:
    if (len(x) == len(y)):
        lst_x = list(map(lambda r: r - (sum(x) / len(x)), x))
        print(lst_x)
        lst_y = list(map(lambda f: f - (sum(y) / len(y)), y))
        print(lst_y)
        try:
            return sum(list(r * f for r, f in zip(lst_x, lst_y))) / \
            (math.sqrt(sum(list((r ** 2) * (f ** 2) for r, f in zip(lst_x, lst_y)))))
        except ZeroDivisionError:
            return None
    else:
        return None


def p_c(x: list[int], y: list[int]) -> float | None:
    upper = 0
    down = 0
    avg_x = sum(x) / len(x)
    avg_y = sum(y) / len(y)
    for i in range(0, len(x)):
        n = (x[i] - avg_x) * (y[i] - avg_y)
        upper += n
        f = ((x[i] - avg_x) ** 2) * ((y[i] - avg_y) ** 2)
        down += f
    down = math.sqrt(down)
    return upper / down


print(pearson_correlation([1, 2, 3], [10, 20, 29]))
print(p_c([1, 2, 3], [10, 20, 29]))

print(pearson_correlation([1, 2, 3, 4, 5], [2, 3, 6, 8, 10]))
print(p_c([1, 2, 3, 4, 5], [2, 3, 6, 8, 10]))
