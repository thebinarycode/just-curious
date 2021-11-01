from collections import Counter


def frame_array(arr: list) -> list:
    """The goal is to sort elements of array by its frequency of elements in decreasing order, without duplication
    Example:
        input[] = [4, 4, 5, 6, 4, 2, 2, 2, 5, 8, 5], output[] = [5, 4, 2, 8, 6]"""

    sorted_map = {key: value for key, value in sorted(Counter(arr).items(), key=lambda item: item[1], reverse=True)}
    print(sorted_map)
    keys = list(sorted_map.keys())

    result = []
    prev_key = []
    prev_val = 0
    print(len(sorted_map))
    for i, key in enumerate(sorted_map.keys()):
        if prev_val == 0:
            prev_val = sorted_map.get(key)
            prev_key.append(key)
        elif prev_val == sorted_map.get(key):
            prev_key.append(key)
            if i + 1 == len(sorted_map):
                result = sort_append(prev_key, result)
        elif i+1 == len(sorted_map):
            result = sort_append(prev_key, result)
        else:
            result = sort_append(prev_key, result)
            prev_val = sorted_map[key]
            prev_key.clear()
            prev_key.append(key)

    print(result)
    return []

def sort_append(tosort, output):
    tosort.sort(reverse=True)
    output.extend(tosort)
    return output

input = [4, 4, 5, 6, 4, 2, 2, 2, 5, 8, 5]
frame_array(input)