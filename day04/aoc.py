import re
import os
number_extract_pattern = "\\d+"

def part1():
    with open('input.txt') as f:
        lines=f.readlines()
        total_score=0
        for line in lines:
            game = line.split(":")[1].split("|")
            winning_numbers=re.findall(number_extract_pattern,game[0].strip())
            my_numbers=re.findall(number_extract_pattern,game[1].strip())
            matches=0
            print(winning_numbers)
            print(my_numbers)
            for num in my_numbers:
                try:
                    winning_numbers.index(num)
                    matches=matches+1
                    print(f"match {num}")
                except:
                    print(f"no match {num}")
            print(matches)
            score=1
            if matches == 0:
                score=0

            for i in range(matches-1):
                score=score*2

            print(score)
            total_score=total_score+score
        print(total_score)

                






def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        #file_input = [int(x) for x in f.readlines()]
        
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
