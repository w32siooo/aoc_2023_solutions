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
            #print(winning_numbers)
            #print(my_numbers)
            for num in my_numbers:
                try:
                    winning_numbers.index(num)
                    matches=matches+1
                    pass
                except:
                    pass
            #print(matches)
            score=1
            if matches == 0:
                score=0

            for i in range(matches-1):
                score=score*2

            #print(score)
            total_score=total_score+score
        print(total_score)


def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        total_score=0
        hash_map={}
        for i in range (len(lines)):
            hash_map[i+1]=1
        for line in lines:
            
            game_num=int(re.findall(number_extract_pattern,line.split(":")[0].split("|")[0])[0])
            #print(game_num)
            #print(f"running card number: {game_num}")
            game = line.split(":")[1].split("|")
            winning_numbers=re.findall(number_extract_pattern,game[0].strip())
            my_numbers=re.findall(number_extract_pattern,game[1].strip())
            matches=0

            for num in my_numbers:
                try:
                    winning_numbers.index(num)
                    matches=matches+1
                except:
                    pass
            copies=hash_map.get(game_num)
            #print(copies)
            for i in range(matches):
                try:
                    card_to_add=game_num+i+1
                    print(f"won {matches} on card {game_num}  adding card {card_to_add}")
                    times_added= hash_map.get(card_to_add)
                    print(f"times_added: {times_added}")
                    hash_map[card_to_add]=times_added+1*copies
                except:
                    pass
        #print(hash_map)
        for i in range (len(lines)):
            total_score=total_score+hash_map.get(i+1)
        print(total_score)
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
