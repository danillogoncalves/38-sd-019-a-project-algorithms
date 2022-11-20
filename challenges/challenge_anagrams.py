def partition(list_string, start, end):
    pivot = list_string[end]
    delimiter = start - 1

    for index in range(start, end):
        if list_string[index] <= pivot:
            delimiter = delimiter + 1
            list_string[index], list_string[delimiter] = (
                list_string[delimiter],
                list_string[index],
            )

    list_string[delimiter + 1], list_string[end] = (
        list_string[end],
        list_string[delimiter + 1],
    )

    return delimiter + 1


def sorted_string(list_string, start, end):
    if start < end:
        p = partition(list_string, start, end)
        sorted_string(list_string, start, p - 1)
        sorted_string(list_string, p + 1, end)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_list, second_list = list(first_string.lower()), list(
        second_string.lower()
    )

    sorted_string(first_list, 0, len(first_list) - 1)
    sorted_string(second_list, 0, len(second_list) - 1)

    resolved = "".join(first_list) == "".join(second_list)

    return (
        "".join(first_list),
        "".join(second_list),
        resolved,
    )
