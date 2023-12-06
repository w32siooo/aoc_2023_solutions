import re
import os
number_extract_pattern = "\\d+"

def part1():
    with open('input.txt') as f:
        lines=f.readlines()
        times=re.findall(number_extract_pattern,lines[0])
        distances=re.findall(number_extract_pattern,lines[1])
        lengths=[]
        for i in range (len(times)):
            time_left=int(times[i])
            record=int(distances[i])
            list_of_records=[]
            time_left=time_left-1
            speed=1
            for i in range (10000):
                my_distance=time_left*speed
                speed=speed+1
                time_left=time_left-1
                if my_distance > record:
                    list_of_records.append(my_distance)
                
            lengths.append(len(list_of_records))
        total=1
        for length in lengths:
            total=total*length

        print(total)

def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        time=int(''.join(re.findall(number_extract_pattern,lines[0])))
        distance=int(''.join(re.findall(number_extract_pattern,lines[1])))
        time_left=time
        record=distance
        speed=0
        minima=0
        for i in range (time):
            my_distance=time_left*speed
            if my_distance >= record:
                minima=speed
                break
            speed=speed+1
            time_left=time_left-1
        speed=time
        time_left=time-speed
        maxima=time
        for i in range(time, -1, -1):
            my_distance=time_left*speed
            if my_distance >= record :
                maxima=speed
                break
            speed=speed-1
            time_left=time_left+1
        print(maxima-minima+1)


part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
