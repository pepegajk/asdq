#1) Сумма элементов списка:


def sum_list(numbers):
    return sum(numbers)


#2) Поиск наибольшего элемента:


def max_element(numbers):
    return max(numbers)


#3) Удаление дубликатов:


def remove_duplicates(numbers):
    return list(set(numbers))


#4) Объединение списков:


def merge_lists(list1, list2):
    return list1 + list2


#5) Поиск элемента в кортеже:


def find_element(tup, element):
    if element in tup:
        return tup.index(element)
    else:
        return "Element not found"


#6) Слияние кортежей:


def merge_tuples(tup1, tup2):
    return tup1 + tup2


#7) Удаление элемента из кортежа:


def remove_element(tup, element):
    # Convert tuple to list to remove element
    l = list(tup)
    if element in l:
        l.remove(element)
        # Convert list back to tuple
        return tuple(l)
    else:
        return "Element not found"

#8) Подсчет элементов в кортеже:


def count_element(tup, element):
    return tup.count(element)
