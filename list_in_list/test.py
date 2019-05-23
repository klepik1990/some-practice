def main():
    a = [1, 2, 3, [2, 34, [12, {'DO': 1, 'THE': 2}, 19]], (1, 2, 3), "Kek"]
    start_result = []
    k = merge(a, start_result)
    print(k)


def merge(construct, result=[]):
    try:
        for elem_of_const in construct:
            if isinstance(elem_of_const, (list, tuple, set)):
                merge(elem_of_const, result)
            elif isinstance(elem_of_const, dict):
                elem_of_const = dict_to_list(elem_of_const)
                for elem in elem_of_const:
                    result.append(elem)
            else:
                result.append(elem_of_const)
        print(result)
        return result
    except EOFError:
        print(EOFError)


def dict_to_list(some_dict):
    temp = []
    dict_list = []
    for key, value in some_dict.items():
        temp.extend((key, value))
    dict_list.extend(temp)
    return dict_list


def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return None


if __name__ == '__main__':
    main()