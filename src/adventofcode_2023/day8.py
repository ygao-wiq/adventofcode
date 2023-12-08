import math
import utils


def Least_common_multiple(num):  # 求任意多个数的最小公倍数
    minimum = 1
    for i in num:
        minimum = int(i)*int(minimum) / math.gcd(int(i), int(minimum))
    return int(minimum)

def Maximum_common_divisor(num):  # 求任意多个数的最大公约数
    minimum = max(num)
    for i in num:
        minimum = math.gcd(int(i), int(minimum))
    return int(minimum)

def solution_1():
    data_lines = utils.get_file_content("day8.dat")
    instructions = data_lines[0].strip()
    i = 2
    node_map: dict[str, (str, str)] = dict()
    while i<len(data_lines):
        pairs = data_lines[i].split(" = ")
        node_map[pairs[0].strip()] = tuple(pairs[1][1:-2].split(", "))
        i += 1
    key = "AAA"
    end = "ZZZ"
    i = 0
    while True:
        if instructions[i%len(instructions)] == "L":
            next = node_map[key][0]
        else:
            next = node_map[key][1]
        if next == "ZZZ":
            break
        key = next
        i = i+1
    print (i+1)
    
def solution_2():
    data_lines = utils.get_file_content("day8.dat")
    instructions = data_lines[0].strip()
    i = 2
    node_map: dict[str, (str, str)] = dict()
    start_points = set()
    while i<len(data_lines):
        pairs = data_lines[i].strip().split(" = ")
        node_map[pairs[0].strip()] = tuple(pairs[1][1:-1].split(", "))
        if pairs[0].strip().endswith("A"):
            start_points.add(pairs[0].strip())
        i += 1
    each_key_steps = list()
    for key in start_points:
        next = key
        i = 0
        while True:
            if instructions[i%len(instructions)] == "L":
                next = node_map[next][0]
            else:
                next = node_map[next][1]
            if next.endswith("Z"):
                break
            i = i+1
        each_key_steps.append(i+1)
    print(Least_common_multiple(each_key_steps))

if __name__ == "__main__":
    solution_1()
    solution_2()