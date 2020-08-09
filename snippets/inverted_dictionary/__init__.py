"""
Every now and again you may encounter a need to invert a dictionary (swap keys with values).

Here is one way you can go about it.
"""

from collections import defaultdict, namedtuple


TypeFunctionMap = namedtuple('TypeFunctionMap', ['type', 'function'])


class DictType:
    """
    Cast function lookup.
    """

    list = TypeFunctionMap(list, list.append)
    set = TypeFunctionMap(set, set.add)
    str = TypeFunctionMap(str, None)
    int = TypeFunctionMap(int, None)
    float = TypeFunctionMap(float, None)


input_dictionary = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": list([1, 2, 3]),
    "key_4": {4, 5, 6},
    "key_5": 1
}


def invert_dict(input_dict, dict_type):
    """
    Invert dictionary.

    :param input_dict: Input dictionary.
    :type input_dict: dict
    :param dict_type: Cast function to apply to dictionary keys.
    :type dict_type: TypeFunctionMap
    :return: Inverted dictionary.
    :rtype: dict
    """

    output = defaultdict(dict_type.type)

    for key, value in input_dict.items():
        if hasattr(value, '__iter__') and not isinstance(value, str):
            for item in value:
                if dict_type.function:
                    dict_type.function(output[item], key)
                else:
                    output[item] = key
        else:
            if dict_type.function:
                dict_type.function(output[value], key)
            else:
                output[value] = key

    return dict(output)


print(invert_dict(input_dictionary, DictType.list))
print(invert_dict(input_dictionary, DictType.set))
print(invert_dict(input_dictionary, DictType.str))
