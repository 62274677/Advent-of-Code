import os
import sys
from operator import methodcaller

def readfile(file_path):
    file = open(file_path,'r')
    input_rounds = file.read().split("\n")
    # print(len(input_calories))
    
    
    # elf_cals = input_calories.split('\n\n')
    # print(len(elf_cals))
    # elf_cals = list(map(methodcaller("split","\n"),elf_cals))
    # print(len(elf_cals))
    # print(elf_cals)
    return input_rounds
def find_result(opponent, round_result):
    values = [
        ("ROCK", 'A', 'B', 1), # NAME, TAG, LOSES TO, VALUE
        ("PAPER", 'B', 'B', 2),
        ("SCISSORS", 'C', 'A', 3),
        
    ]
    
    if round_result == 'Z': # WIN
        for value in values:
            if value[1] == opponent:
                return value[2]
    elif round_result == 'X':
        for value in values:
            if value[2] == opponent:
                return value[2]
            
    print("Error: opponent value not found.")
    return -1
        
        
        
    

def force_result(opponent,round_result):
    if round_result == "Y":
        return round_value(opponent, opponent)
    elif round_result == "":
        pass
        
        

def round_value(opponent, protag):
    values = [
        ("ROCK", 'A', 'B', 1), # NAME, TAG, LOSES TO, VALUE
        ("PAPER", 'B', 'C', 2),
        ("SCISSORS", 'C', 'A', 3),
        
    ]
    
    opponent_point = get_point_opponent(values,opponent)
    protag_point = get_point_protag(values, protag) #! SET THIS TO SAME AS OPPONENT
    
    if opponent_point == -1 or protag_point == -1:
        return -1
    if opponent_point == protag_point:
        return protag_point+3
    
    if opponent_point == 1:
        if protag_point == 2:
            return protag_point+6
            # won
        else:
            return protag_point
            # lost
    elif opponent_point == 2:
        if protag_point == 3:
            return protag_point+6
            # won
        else:
            return protag_point
            # lost
        
    elif opponent_point == 3:
        if protag_point == 1:
            return protag_point+6
            # won
        else:
            return protag_point
            # lost
    
    
    
def get_point_opponent(values, hand):
    for value in values:
        if value[1] == hand:
            return value[3]
    print("Error: opponent value not found.")
    return -1

def get_point_protag(values, hand):
    for value in values:
        if value[2] == hand:
            return value[3]
    print("Error: protag value not found.")
    return -1

def get_name_opponent(values, hand):
    for value in values:
        if value[1] == hand:
            return value[0]
    print("Error: opponent name not found.")
    return -1

def get_name_protag(values, hand):
    for value in values:
        if value[2] == hand:
            return value[0]
    print("Error: protag name not found.")
    return -1

    
rounds = readfile("input.txt")
round_points = []
for round in rounds:
    # print(round.split(" ")[0])
    round_results = round.split(" ")
    round_point = check_win(round_results[0], round_results[1])
    round_points.append(round_point)
    # print("Opponent threw {}{} against our {}{} resulting in {} points".format(round_results[0]))
print(sum(round_points))
    
    