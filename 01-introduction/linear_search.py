def linear_search(_list, item):
    index = 0
    list_length = len(_list) - 1
    while index <= list_length:
        searched_item = _list[index]
        if searched_item == item:
            return index
        else:
            index += 1
    return None

flat_list = [1, 2, 6, 4, 9, 10, 20]


print(linear_search(flat_list, 10))