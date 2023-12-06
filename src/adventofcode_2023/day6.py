import math
import utils

def parse_data(data_lines: list[str]) -> list[tuple[int, int]]:
    ret = list()
    time_lst = [int(e) for e in data_lines[0].lstrip("Time:").split(" ") if len(e)>0]
    distance_lst = [int(e) for e in data_lines[1].lstrip("Distance:").split(" ") if len(e)>0]
    return list(zip(time_lst, distance_lst))

def parse_data2(data_lines: list[str]) -> tuple[int, int]:
    ret = list()
    time_lst = [e for e in data_lines[0].lstrip("Time:").split(" ") if len(e)>0]
    distance_lst = [e for e in data_lines[1].lstrip("Distance:").split(" ") if len(e)>0]
    time_value = "".join(time_lst)
    distance_value = "".join(distance_lst)
    return int(time_value), int(distance_value)

def solution_1():
    data_lines = utils.get_file_content("day6.dat")
    races_data = parse_data(data_lines)
    ways_to_win = list()
    for t, d in races_data:
        temp_ways_win = 0
        for charge_time in range(t):
            if charge_time * 1 * (t-charge_time) > d:
                temp_ways_win += 1
        ways_to_win.append(temp_ways_win)
    print(math.prod(ways_to_win))

def solution_2():
    data_lines = utils.get_file_content("day6.dat")
    time_data, distance_data = parse_data2(data_lines)

    temp_ways_win = 0
    for charge_time in range(time_data):
        if charge_time * 1 * (time_data-charge_time) > distance_data:
            temp_ways_win += 1

    print(temp_ways_win)

def solution_2_2():
    # quadratic function method
    data_lines = utils.get_file_content("day6_sample.dat")
    time_data, distance_data = parse_data2(data_lines)

    temp_ways_win = 0
    s1 = (time_data+math.sqrt(time_data**2-4*distance_data))/2
    s2 = (time_data-math.sqrt(time_data**2-4*distance_data))/2
    temp_ways_win = math.floor(s1) - math.ceil(s2) + 1
    print(temp_ways_win)
    
if __name__ == "__main__":
    solution_1()
    #solution_2()
    solution_2_2()