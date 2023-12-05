import re
import os
number_extract_pattern = "\\d+"

def part1():
    with open('input.txt') as f:
        lines=f.readlines()
        total_score=0
        maps_list=[]
        range_map_list=[]
        parse=False
        newMap={}
        range_map={}
        #key = newMap
        #value
        seeds=""
        lines.append("/n")
        for line in lines:
            if len(re.findall(number_extract_pattern,line))>0 and not line.startswith("seeds:"):
                tmp=line.strip().split(" ")
                range_key = (int(tmp[2]))
                source=int(tmp[1])
                dest=int(tmp[0])
                newMap[source]=dest
                range_map[counter]=range_key
                counter=counter+1
            else:
                range_map_list.append(range_map)
                maps_list.append(newMap)
                range_map={}
                newMap={}
                counter=0
            if line.startswith("seeds"):
                seeds=line.split(":")[1].strip().split(" ")

        final_locs=[]
        for seed in seeds:
            seed=int(seed)

            for map_index in range (len(maps_list)):
                curr_map = maps_list[map_index]
                #print(curr_map)
                cnt=0
                a_match=True
                for source in curr_map:
                    dest=curr_map[source]
                    rng=range_map_list[map_index][cnt]
                    #print(f"src: {source} dest: {dest} range {rng}")
                    min_rng=source
                    max_rng=source+(rng-1)
                    
                    if min_rng <= seed <= max_rng:
                        seed=dest-(source-seed)
                        a_match=False
                        break
                    if a_match != True:
                        continue
                    
                    cnt=cnt+1
                

            final_locs.append(seed)

        print(min(final_locs))

            

def part2():
    with open('test.txt') as f:
        print("not sure yet")
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
