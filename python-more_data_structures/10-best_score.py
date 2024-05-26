#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sorted_dict = sorted(a_dictionary)
    sorted_dict_list = list(sorted_dict)
    return sorted_dict_list[-1]
