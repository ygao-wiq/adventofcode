import sys

import utils

seed_lst = list()
seed_to_soil_maps = dict()
soil_to_fertilizer = dict()
fertilizer_to_water = dict()
water_to_light = dict()
light_to_temperature = dict()
temperature_to_humidity = dict()
humidity_to_location = dict()

total_maps = {
    "seed-to-soil": seed_to_soil_maps,
    "soil-to-fertilizer": soil_to_fertilizer,
    "fertilizer-to-water": fertilizer_to_water,
    "water-to-light": water_to_light,
    "light-to-temperature": light_to_temperature,
    "temperature-to-humidity": temperature_to_humidity,
    "humidity-to-location": humidity_to_location,
}


class Range(object):
    def __init__(self, start, length):
        self.start = start
        self.length = length

    def is_in_range(self, x: int) -> bool:
        return self.start <= x <= self.start + self.length - 1

    def get_value_offset(self, x: int) -> int:
        if self.is_in_range(x):
            return x - self.start
        else:
            return -1

    def get_target_value(self, offset: int) -> int:
        return self.start + offset


def parse_data(data_lines: list[str]):
    i = 0
    while i < len(data_lines):
        target_dict = None
        if data_lines[i].startswith("seeds:"):
            seed_lst.extend([int(d) for d in data_lines[i].split("seeds:")[1].strip().split(" ") if len(d) > 0])
            i += 1
        elif data_lines[i].endswith("map:"):
            target_dict = total_maps[data_lines[i].split(" ")[0]]
            i += 1
            while i < len(data_lines):
                if len(data_lines[i]) == 0:
                    target_dict = None
                    i += 1
                    break
                else:
                    (dest, source, length) = data_lines[i].split(" ")
                    target_dict[Range(int(source), int(length))] = Range(int(dest), int(length))
                    i += 1
        else:
            i += 1


def get_next_value(value, search_map: dict[Range, Range]) -> int:
    for k, v in search_map.items():
        if k.get_value_offset(value) != -1:
            return v.get_target_value(k.get_value_offset(value))
    return value


def solution_1():
    data_lines = [l.strip() for l in utils.get_file_content("day5.dat")]
    parse_data(data_lines)
    ret = sys.maxsize
    for seed in seed_lst:
        src = seed
        for k in total_maps.keys():
            search_map = total_maps[k]
            src = get_next_value(src, search_map)
        ret = min(ret, src)
    print(ret)


def solution_2():
    data_lines = [l.strip() for l in utils.get_file_content("day5.dat")]
    parse_data(data_lines)
    ret = sys.maxsize
    local_seed_lst = list(zip(seed_lst[0::2], seed_lst[1::2]))
    for start_seed, seed_length in local_seed_lst:
        start_seed_i = start_seed
        while start_seed_i < start_seed+seed_length:
            src = start_seed_i
            for k in total_maps.keys():
                search_map = total_maps[k]
                src = get_next_value(src, search_map)
            ret = min(ret, src)
            start_seed_i += 1
    print(ret)


if __name__ == "__main__":
    solution_1()
    seed_lst.clear()
    for k, v in total_maps.items():
        v.clear()
    solution_2()
