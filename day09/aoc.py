import os
def custom_len(start, stop):
    return  stop-start
def find_diff_matrix(ex,result=None):
    if result is None:
        result = []
    diffs=[]
    for ins in range(len(ex)-1): 
        calculation = custom_len(ex[ins+1],ex[ins])
        diffs.append(calculation)
    result.append(diffs)
    if all(element == 0 for element in diffs):
        return result
    else:
        return find_diff_matrix(diffs,result)

def find_diff_matrix_p2(ex,result=None):
    if result is None:
        result = []
    diffs=[]
    for ins in range(len(ex)-1): 
        calculation = custom_len(ex[ins],ex[ins+1])
        diffs.append(calculation)
    result.append(diffs)
    if all(element == 0 for element in diffs):
        return result
    else:
        return find_diff_matrix_p2(diffs,result)

def fill_out_res(res):
    counter=0
    for array in reversed(res):
        if counter==0:
            res[len(res)-1].append(0) ## add zero to bottom array
        else:
            bottom=+res[len(res)-counter][-1]
            upper= res[len(res)-counter-1][-1]
            to_add=upper-bottom
            res[-counter-1].append(to_add) #array just above
        counter+=1
    return res[0][-1]

def fill_out_res_p2(res):
    counter=0
    for array in reversed(res):
        if counter==0:
            res[len(res)-1].insert(0,0) ## add zero to bottom array
        else:
            bottom=+res[len(res)-counter][0]
            upper= res[len(res)-counter-1][0]
            to_add=upper-bottom
            res[-counter-1].insert(0,to_add) #array just above
        counter+=1

    return res[0][0]

def part1():

    with open('input.txt') as f:
        lines=f.readlines()
        total=0
        for line in lines:
            ex = [int(x) for x in line.split(" ")]
            diff_matrix = find_diff_matrix(ex)
            diff_matrix.insert(0,ex)
            res= fill_out_res(diff_matrix)
            total+=res
        return total

def part2():
    with open('input.txt') as f:
        lines=f.readlines()
        total=0
        for line in lines:
            ex = [int(x) for x in line.split(" ")]
            diff_matrix = find_diff_matrix_p2(ex)
            diff_matrix.insert(0,ex)
            res= fill_out_res_p2(diff_matrix)
            total+=res
        return total

part = os.environ.get('part')
if part == "part1":
    part1()
if part == "part2":
    part2()
