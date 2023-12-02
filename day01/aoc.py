import re
number_extract_pattern = "\\d+"
import os
def part1():
    with open('input.txt') as f:
        lines=f.readlines()
        #file_input = [int(x) for x in f.readlines()]
        first_digit=0
        last_digit=0
        total=0
        
        digitlist=["0","1","2","3","4","5","6","7","8","9"]
        for line in lines:

            str_matches= re.findall(r"(?=("+'|'.join(digitlist)+r"))", line)
        
            first_digit = str(str_matches[0])
            try :
                last_digit = str(str_matches[-1])
            except:
                last_digit=first_digit
            try:
                int(first_digit)
            except:
                first_digit=digitlist.index(first_digit)-10
            try:
                int(last_digit)
            except:
                last_digit=digitlist.index(last_digit)-10

            combined=int(str(first_digit)+str(last_digit))

            total=total+combined
        print(total)
def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        #file_input = [int(x) for x in f.readlines()]
        first_digit=0
        last_digit=0
        total=0
        
        digitlist=["0","1","2","3","4","5","6","7","8","9","zero","one","two","three","four","five","six","seven","eight","nine"]
        for line in lines:

            str_matches= re.findall(r"(?=("+'|'.join(digitlist)+r"))", line)
        
            first_digit = str(str_matches[0])
            try :
                last_digit = str(str_matches[-1])
            except:
                last_digit=first_digit
            try:
                int(first_digit)
            except:
                first_digit=digitlist.index(first_digit)-10
            try:
                int(last_digit)
            except:
                last_digit=digitlist.index(last_digit)-10

            combined=int(str(first_digit)+str(last_digit))
            total=total+combined
        print(total)
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()

        
