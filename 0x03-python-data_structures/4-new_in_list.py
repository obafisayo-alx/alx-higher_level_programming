#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if (my_list):
        new_list = []
        for i in my_list:
            new_list.append(my_list[i - 1])
    if idx < 0 or idx >= len(my_list):
        return (new_list)
    new_list[idx] = element
    return (new_list)
