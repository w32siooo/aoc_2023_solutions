import re
import os
number_extract_pattern = "\\d+"

def part1():
    with open('test.txt') as f:
        lines=f.readlines()
        total_score=0
        seed_to_soil=False
        soil_to_fertilizer=False
        f_2_w=False
        w_2_l=False
        l_2_t=False
        t_2_h=False
        h_2_l=False
        seed_to_soil_map={}
        soil_to_fertilizer_map={}
        f_2_w_map={}
        w_2_l_map={}
        l_2_t_map={}
        t_2_h_map={}
        h_2_l_map={}
        for line in lines:
            if line.startswith("\n"):
                seed_to_soil=False
                soil_to_fertilizer=False
                f_2_w=False
                w_2_l=False
                l_2_t=False
                t_2_h=False
                h_2_l=False
                tmp=None
            if line.startswith("seeds"):
                seeds=line.split(":")[1].strip().split(" ")
                print(f"seeds: {seeds}")
            if seed_to_soil:
                tmp=line.strip().split(" ")
                print(f"seed to soil: {tmp}")
                for i in range (int(tmp[2])):
                    source=int(tmp[1])+i
                    dest=int(tmp[0])+i
                    seed_to_soil_map[source]=dest
            if soil_to_fertilizer:
                tmp=line.strip().split(" ")
                print(f"soil_to_fertilizer: {tmp}")
            if f_2_w:
                tmp=line.strip().split(" ")
                print(f"fert 2 water: {tmp}")
            if w_2_l:
                tmp=line.strip().split(" ")
                print(f"w_2_l: {tmp}")
            if l_2_t:
                tmp=line.strip().split(" ")
                print(f"seed to soil: {tmp}")
            if t_2_h:
                tmp=line.strip().split(" ")
                print(f"t_2_h_map: {tmp}")
            if h_2_l:
                tmp=line.strip().split(" ")
                print(f"h_2_l_map: {tmp}")
            if line.startswith("seed-to-soil map"):
                seed_to_soil=True
            if line.startswith("soil-to-fertilizer map"):
                soil_to_fertilizer=True
            if line.startswith("fertilizer-to-water map"):
                f_2_w=True
            if line.startswith("water-to-light map"):
                w_2_l=True
            if line.startswith("light-to-temperature map"):
                l_2_t=True
            if line.startswith("temperature-to-humidity map"):
                t_2_h=True
            if line.startswith("humidity-to-location map"):
                h_2_l=True
            print(seed_to_soil_map)
            
            
# Consider again the example seed-to-soil map:

# 50 98 2
# 52 50 48
#The first line has a destination range start of 50, a source range start of 98, and a range length of 2. 
# This line means that the source range starts at 98 and contains two values: 98 and 99.
#  The destination range is the same length, but it starts at 50, so its two values are 50 and 51.
#  With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.



#a destination range start of 50, a source range start of 98, and a range length
#Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.


def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        total_score=0
        print(total_score)
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
part1()
