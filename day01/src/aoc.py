import re
number_extract_pattern = "\\d+"

with open('test.txt') as f:
    lines=f.readlines()
    #file_input = [int(x) for x in f.readlines()]
    first_digit=0
    last_digit=0
    total=0
    
    digitlist=["zero","one","two","three","four","five","six","seven","eight","nine"]

    for line in lines:
        linez=[
        filtered_list = [item for item in linez if str(item).isdigit()]
    
        first_digit = str(filtered_list[0])
        try :
            last_digit = str(filtered_list[-1])
        except:
            last_digit=first_digit
        combined=int(first_digit+last_digit)
        print(combined)

        total=total+combined
    print(total)


        
