#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
     """This replaces the particular element in the list"""
     if (idx < 0 or idx >= len(my_list)):
          return (my_list)
     my_list[idx] = element
     return (my_list)
