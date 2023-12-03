import collections
import math
import utils

def is_machine_part(schematic, left, right, top, bottom):
    i = top
    while i<=bottom:
        j = left
        while j<=right:
            if not (schematic[i][j].isdigit() or schematic[i][j] == "."):
                return True
            j += 1
        i += 1
    return False

def capture_machine_parts(schematic, left, right, top, bottom, gear_ratio_captuer, num):
    i = top
    while i<=bottom:
        j = left
        while j<=right:
            if schematic[i][j] == "*":
                if (i,j) not in gear_ratio_captuer:
                     gear_ratio_captuer[(i,j)] = list()
                gear_ratio_captuer[(i,j)].append(num)
                break
            j += 1
        i += 1

def solution_1():
    data_lines = [l.strip() for l in utils.get_file_content("day3.dat")]
    ret = 0
    schematic = list()
    i = 0
    row_len = len(data_lines)
    while i<len(data_lines):
        line_len = len(data_lines[i])
        top = max(0, i-1)
        bottom = min(i+1, len(data_lines)-1)
        j = 0
        while j<len(data_lines[i]):
            if data_lines[i][j].isdigit():
                num = 0
                left = max(j-1, 0)
                while j<len(data_lines[i]) and data_lines[i][j].isdigit():
                    num = num * 10 + int(data_lines[i][j])
                    j += 1
                right = min(j, len(data_lines[i])-1)
                if is_machine_part(data_lines, left, right, top, bottom):
                    ret += num
            else:
                j += 1
        i += 1
    print(ret)
    
def solution_2():
    data_lines = [l.strip() for l in utils.get_file_content("day3.dat")]
    ret = 0
    i = 0
    
    gear_ratio_captuer = dict()
    
    while i<len(data_lines):
        line_len = len(data_lines[i])
        top = max(0, i-1)
        bottom = min(i+1, len(data_lines)-1)
        j = 0
        while j<len(data_lines[i]):
            if data_lines[i][j].isdigit():
                num = 0
                left = max(j-1, 0)
                while j<len(data_lines[i]) and data_lines[i][j].isdigit():
                    num = num * 10 + int(data_lines[i][j])
                    j += 1
                right = min(j, len(data_lines[i])-1)
                capture_machine_parts(data_lines, left, right, top, bottom, gear_ratio_captuer, num)
            else:
                j += 1
        i += 1
    for v in gear_ratio_captuer.values():
        if len(v) == 2:
            ret += v[0]*v[1]
    print(ret)

    
if __name__ == "__main__":
    solution_1()
    solution_2()