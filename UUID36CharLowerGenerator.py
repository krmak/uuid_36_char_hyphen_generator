# -*- coding: utf-8 -*-
"""
This module contains a Python function to create a random lowercase 36-character 
Universally Unique IDentifier (UUID), where alphanumeric portions of the 
identifier are delimited by four hyphens.
"""

from random import choice

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'

def generate_UUID_36_char_hyphen():
    available_chars = alpha + num
    eight_digit_part_list = []
    four_digit_part1_list = []
    four_digit_part2_list = []
    four_digit_part3_list = []
    twelve_digit_part_list = []
    
    for i in range(8):
        character = choice(available_chars)
        eight_digit_part_list.append(character)
        
    eight_digit_part_str = ''.join(eight_digit_part_list)
    
    for i in range(4):
        character = choice(available_chars)
        four_digit_part1_list.append(character)
        
    four_digit_part1_str = ''.join(four_digit_part1_list)
    
    for i in range(4):
        character = choice(available_chars)
        four_digit_part2_list.append(character)
        
    four_digit_part2_str = ''.join(four_digit_part2_list)

    for i in range(4):
        character = choice(available_chars)
        four_digit_part3_list.append(character)
        
    four_digit_part3_str = ''.join(four_digit_part3_list)

    for i in range(12):
        character = choice(available_chars)
        twelve_digit_part_list.append(character)
        
    twelve_digit_part_str = ''.join(twelve_digit_part_list)

    return eight_digit_part_str + '-' + four_digit_part1_str + '-' + four_digit_part2_str + '-' + four_digit_part3_str + '-' + twelve_digit_part_str               