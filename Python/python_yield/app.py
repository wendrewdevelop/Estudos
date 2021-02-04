def numbers(max_n):
    lst = []

    for number in range(max_n + 1):
        lst.append(number)
    
    return lst


def numbers_yield(max_n):
    for n in range(max_n + 1):
        yield n


gerador = numbers_yield(623 * 10 ** 21)

# Rodar no ipython
next(gerador)