import re
import os

def part1():
    with open('test.txt') as f:
        lines=f.readlines()
        hashmap = {}

        # Adding key-value pairs to the hashmap
        hashmap["key1"] = "value1"
        hashmap["key2"] = "value2"
        hashmap["key3"] = "value3"

        # Accessing values using keys
        print(hashmap["key1"])  # Output: value1
        print(hashmap["key2"])  # Output: value2
        print(hashmap["key3"])  # Output: value3
        #4361


def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        #file_input = [int(x) for x in f.readlines()]
        
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
