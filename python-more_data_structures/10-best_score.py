#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    sorted_dict = dict(sorted(a_dictionary.items(), key=lambda i: i[1]))
    sorted_dict_list = list(sorted_dict)
    return sorted_dict_list[-1]
