import re
import os

def part1():
    with open('test.txt') as f:
        lines=f.readlines()
        hashmap = {}
        y=0
        #load data into map
        for line in lines:
            line=line.strip()
            splitted= [*line]
            x=0
            for split in splitted:
                coord=f"{y},{x}"
                hashmap[coord]=split
                x=x+1
            y=y+1
        
        
        
        print(hashmap)

def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        #file_input = [int(x) for x in f.readlines()]
        
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
part1()