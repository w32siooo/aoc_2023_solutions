import re
import os

def part1():
    with open('input.txt') as f:
        lines=f.readlines()
        #file_input = [int(x) for x in f.readlines()]
        digitlist=["red","green","blue"]
        gamenum=1

        total=0
        for line in lines:
            possible=True
            game=line.split(":")[1]
            #print(game)
            red_res=12 
            green_res=13
            blue_res=14
            bag_list = game.strip().split(";")
            for bag in bag_list:
                
                bagz = bag.strip().split(",")
                #fewest number of cubes of each color that would have made the game possible
                for innerbag in bagz:
                    result_list=[0,0,0]
                    element = innerbag.strip()
                    str_matches= re.findall(r"(?=("+'|'.join(digitlist)+r"))", element) 
                    result_list[digitlist.index(str_matches[0])]=result_list[digitlist.index(str_matches[0])]+int(element.split(" ")[0])
                    if result_list[0]>red_res or result_list[1]>green_res or result_list[2]>blue_res:
                        possible=False
                    
            if possible:
                total=total+gamenum
                #print(gamenum)
            gamenum=gamenum+1
        print(total)


def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        #file_input = [int(x) for x in f.readlines()]
        digitlist=["red","green","blue"]
        gamenum=1

        total=0
        for line in lines:
            possible=True
            game=line.split(":")[1]
            #print(game)
            red_res=12 
            green_res=13
            blue_res=14
            bag_list = game.strip().split(";")
            result_list=[0,0,0]
            for bag in bag_list:
                bagz = bag.strip().split(",")
                #fewest number of cubes of each color that would have made the game possible
                for innerbag in bagz:
                    element = innerbag.strip()
                    str_matches= re.findall(r"(?=("+'|'.join(digitlist)+r"))", element) 
                    incoming_element=int(element.split(" ")[0])
                    current_element=result_list[digitlist.index(str_matches[0])]
                    if current_element < incoming_element:
                        result_list[digitlist.index(str_matches[0])]=incoming_element
                    
            total=total+result_list[0]*result_list[1]*result_list[2]
            gamenum=gamenum+1
        print(total)
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
