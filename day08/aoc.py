import re
letter_extract_pattern = "\\w+"
from math import lcm
import os
def part1():
    with open('input.txt') as f:
        lines=f.readlines()
        instructions=[*lines[0].strip()]
        lines=lines[2:]
        instruction_map= {}
        for line in lines:
            res = re.findall(letter_extract_pattern,line)
            instruction_map[res[0]]=(res[1],res[2])
        
        steps=0
        instructions_index=0
        current_hash='AAA'
        while current_hash != "ZZZ":
            current_hash = instruction_map[current_hash][0] if instructions[instructions_index] == "L" else instruction_map[current_hash][1]
            steps+=1
            instructions_index += 1
            instructions_index %= len(instructions)
        print(steps)

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
        instructions = [*lines[0].strip()]
        lines = lines[2:]
        instruction_map = {}
        node_list = []

        for line in lines:
            res = re.findall(letter_extract_pattern, line)
            instruction_map[res[0]] = res[1], res[2]
            if res[0].endswith('A'): 
                node_list.append(res[0])

        steps = 0
        instructions_index = 0
        steps_till_z=[]
        for node in node_list:
            steps=0
            instructions_index=0
            while not node.endswith('Z'):
                node = instruction_map[node][0] if instructions[instructions_index] == "L" else instruction_map[node][1]
                steps += 1
                instructions_index += 1
                instructions_index %= len(instructions)
            steps_till_z.append(steps)
        print(lcm(*steps_till_z))

part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()