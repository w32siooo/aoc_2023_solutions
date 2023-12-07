import re
import os
number_extract_pattern = "\\d+"

def part1():
    with open('input.txt') as f:
        lines=f.readlines()
        cards=["0","1","2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        cards_with_qualities={}
        counter=0
        for line in lines:
            hand = line.split(" ")[0]
            bet= int(line.split(" ")[1])
            
            quality=None
            hand_card_indexes=[]
            unsorted_hand=[]
            
            for card in hand:
                index=cards.index(card)
                hand_card_indexes.append(index)
                unsorted_hand.append(index)
            
            hand_card_indexes.sort()

            prev=None
            matches={}
            for card in hand_card_indexes:
                if card == prev :
                    try:
                        matches[card]=matches[card]+1
                    except:
                        matches[card]=2
                prev=card

            if len(matches)==0:
                highest_card=hand_card_indexes[-1]
                quality=1
            
            if len(matches)==2:
                full_house_checker=0
                for match in matches:
                    full_house_checker=full_house_checker+matches[match]
                if full_house_checker==5:
                    quality=5
                else:

                    quality=3

            
            if len(matches)==1:
                for match in matches:
                    of_a_kind=matches[match]
                    if of_a_kind == 5:
                        quality=7
                    if of_a_kind == 4:
                        quality=6
                    if of_a_kind == 3:
                        quality=4
                    if of_a_kind == 2:
                        quality=2
                    
            cards_with_qualities[counter]=(quality,unsorted_hand,bet)
            counter=counter+1
        sorted_hashmap = dict(sorted(cards_with_qualities.items(), key=custom_sort,reverse=True))

        rank=1
        total=0
        for a_map in sorted_hashmap:
            bet=sorted_hashmap[a_map][2]
            total=total+(bet*rank)
            rank=rank+1
        return total #250957639 rght

def custom_sort(item):
    score=0
    index=1
    for ele in item[1][1]:
        score=score+(ele*index)
        index=index*0.010

    return (-item[1][0],-score)


def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        cards=["J","1","2","3","4","5","6","7","8","9","T","Q","K","A"]
        cards_with_qualities={}
        counter=0
        for line in lines:
            #str_matches= re.findall(r"(?=("+'|'.join(cards)+r"))", line)
            hand = line.split(" ")[0]
            bet= int(line.split(" ")[1])
            #get jokers
            jokers=0
            jokers=len(re.findall("J",hand))
            quality=1
            hand_card_indexes=[]
            unsorted_hand=[]
            
            for card in hand:
                index=cards.index(card)
                hand_card_indexes.append(index)
                unsorted_hand.append(index)
            
            hand_card_indexes.sort()

            prev=None
            matches={}
            for card in hand_card_indexes:
                if card == prev :
                    try:
                        matches[card]=matches[card]+1
                    except:
                        matches[card]=2
                prev=card
            
            highest_card=hand_card_indexes[-1]

            for card in unsorted_hand:
                if card==0: 
                    try:
                        of_a_kind=matches[card]
                    except:
                        of_a_kind=jokers
                else:
                    try:
                        of_a_kind=matches[card]+jokers
                    except:
                        of_a_kind=1+jokers
                
                if of_a_kind >= 5 :
                    quality=7
                if of_a_kind == 4 and quality<6:
                    quality=6
                if of_a_kind == 3 and quality<4:
                    quality=4
                if of_a_kind == 2 and quality<2:
                    quality=2
            if len(matches)==2:
                full_house_checker=0
                for match in matches:
                    full_house_checker=full_house_checker+matches[match]
                if jokers==0 and full_house_checker==5:
                    quality=5
                if quality < 3:
                    quality=3
                if jokers==1 and quality<5:
                    quality=5


            cards_with_qualities[counter]=(quality,unsorted_hand,bet)
            counter=counter+1

        sorted_hashmap = dict(sorted(cards_with_qualities.items(), key=custom_sort,reverse=True))

        rank=1
        total=0
        for a_map in sorted_hashmap:
            bet=sorted_hashmap[a_map][2]
            total=total+(bet*rank)
            rank=rank+1
        return total  

part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()

assert  part1() ==250957639
assert part2() == 251515496
#251515496 