import math

def binary_search(ranged_list, item):
    low = 0
    high = len(ranged_list) - 1

    while low <= high:
        medium = math.ceil((low + high) / 2)
        attempt = ranged_list[medium]

        if attempt == item:
            return medium
        if attempt > item:
            high = medium - 1
        else:
            low = medium + 1

    return None

example_list = [1, 3, 5, 7, 9]

print(binary_search(example_list, 3))
print(binary_search(example_list, -1))