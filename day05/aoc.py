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
        lines=f.readlines()
        total_score=0
        maps_list=[]
        range_map_list=[]
        newMap={}
        range_map={}
        lines.append("/n")
        seeds=""
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
                
        seed_ranges=[]
        for i in range(len(seeds)):

            if i % 2 == 0:
                master=seeds[i]
            else:
                rng=seeds[i]
                seed_ranges.append((master,rng))
                master=0
                rng=0

        final_locs=[99999999999999999]
        for seed_tuple in seed_ranges:
            print(seed_tuple)
            counter=0
            seed=int(seed_tuple[0])
            seed_range=range(int(seed_tuple[1]))
            for i in seed_range:
                
                seed=int(seed_tuple[0])+counter

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
                if seed < min(final_locs):
                    final_locs.append(seed)
                else:
                    continue
                #print("===========")
                counter=counter+1
                

        #print(maps_list)
        print(f"lowest loc: {min(final_locs)}")
part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
