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

def is_range_within_another(inner_range, outer_range):
    try:
        range(max(inner_range[0], outer_range[0]), min(inner_range[-1], outer_range[-1])+1)
    except:
        return False

def find_lowest_common_integer(range1, range2):
    start = max(range1.start, range2.start)
    stop = min(range1.stop, range2.stop)
    if start < stop:
        return start
    else:
        return None


            

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

        final_locs=[]
        for seed_tuple in seed_ranges: ### roll the seed ranges
            print(seed_tuple)
            seed=int(seed_tuple[0])
            seed_range=range(seed,int(seed_tuple[1]))
            
            
            for map_index in range (len(maps_list)): ### iterate over the maps
                curr_map = maps_list[map_index]
                #print(curr_map)
                count=0
                a_match=True
                for source in curr_map: ### iterate over source list in maps
                    dest=curr_map[source]
                    rng=range_map_list[map_index][count]
                    seed_max=seed+int(seed_tuple[1])
                    source_range=range(source,source+(rng-1))
                    print(f"{source_range}, {seed_range}")
                    if is_range_within_another(source_range,seed_range):
                        hello=find_lowest_common_integer(source_range,seed_range)
                        print(f"lowest overlap: {hello}")
                        
                        seed=dest-(source-hello)
                        a_match=False
                        break
                    if a_match != True:
                        continue
                    count=count+1
            final_locs.append(seed)
            #print("===========")
            counter=counter+1
            
        #print(maps_list)
        print(f"lowest loc: {min(final_locs)}")

part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
part2()