import os
import sys
from operator import methodcaller

debug = False
def readfile(file_path):
    file = open(file_path,'r')
    input_calories = file.read()
    # print(len(input_calories))
    elf_cals = input_calories.split('\n\n')
    print(len(elf_cals))
    elf_cals = list(map(methodcaller("split","\n"),elf_cals))
    # print(len(elf_cals))
    # print(elf_cals)
    return elf_cals


# top_elfs_count = 3
def iterative_sumcals(elf_cals,top_elfs_count=3):
    current_elf = 0
    biggest_elfs = []
    for elf in elf_cals:
        cal_sum = 0
        current_elf+=1
        
        for cal in elf:
            cal_sum+=int(cal)
            
        if len(biggest_elfs)==0:
            biggest_elfs.append(cal_sum)
        else:
            for index, elf in enumerate(biggest_elfs):
                
                if cal_sum >= elf and len(biggest_elfs)>=top_elfs_count:
                    if debug: print("old array correct size: ", biggest_elfs)
                    
                    biggest_elfs.insert(index,cal_sum)
                    biggest_elfs.pop(top_elfs_count)
                    if debug: print("added ", cal_sum, " to index [", index,"], new array: ",biggest_elfs  )
                    break
                elif len(biggest_elfs)<top_elfs_count and index == len(biggest_elfs)-1:  # cal_sum>= elf and :
                    if debug: print("old array small: ", biggest_elfs)
                    biggest_elfs.append(cal_sum)
                    if debug: print("added ", cal_sum, " to index [", index,"], new array: ",biggest_elfs  )
                    break
                if debug: print(cal_sum, " is no bigger than ", elf)
    return biggest_elfs
            
def map_sumcal(elf_cals,top_elfs_count=3):            
    elf_cals_nums = []
    all_sums = ()
    for elf in elf_cals:
        elf_cals_nums.append(list(map(int,elf)))
    all_sums = list(map(sum,elf_cals_nums))
    all_sums.sort()
    if debug: print("all sums: ", all_sums)
    return all_sums[-1*top_elfs_count:]

def arian_death():
    with open("/tmp/input.txt", 'r') as f:
        sorted_calories = sorted((
            sum(map(int, elf.split('\n'))) #3 
            for elf in f.read().split("\n\n") #1 for line in file split on elfs
            if '' not in elf.split('\n') #2 if '' 
        ), reverse=True)
    return sorted_calories

elf_cals = readfile("input.txt")
all_sums = map_sumcal(elf_cals,top_elfs_count=3)
print(all_sums)
print(sum(all_sums))

biggest_elfs=iterative_sumcals(elf_cals,top_elfs_count=3)        
print(biggest_elfs)
print(sum(biggest_elfs))

    
    
    


