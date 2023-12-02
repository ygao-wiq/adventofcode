import collections
import math
import utils

game_data = collections.namedtuple("game_data", ["red", "green", "blue"])

def game_data_extractor(s: str) -> (int, [game_data]):
    id_data_pair = s.split(":")
    game_id = int(id_data_pair[0].strip().lstrip("Game "))
    data = list()
    for e in id_data_pair[1].split(";"):
        red = 0
        green = 0
        blue = 0
        for e1 in e.strip().split(","):
            if e1.endswith("red"):
                red = int(e1.strip().split(" ")[0])
            elif e1.endswith("green"):
                green = int(e1.strip().split(" ")[0])
            elif e1.endswith("blue"):
                blue = int(e1.strip().split(" ")[0])
        data.append(game_data(red=red, green=green, blue=blue))
    return (game_id, data)


def solution_1():
    data_lines = utils.get_file_content("day2.dat")
    ret = 0
    red_cap = 12
    green_cap = 13
    blue_cap = 14
    for l in data_lines:
        game_id, game_data = game_data_extractor(l)
        if all([True if d.red<=red_cap and d.green<=green_cap and d.blue<=blue_cap else False for d in game_data]):
            ret += game_id
    print(ret)
    
def solution_2():
    data_lines = utils.get_file_content("day2_sample.dat")
    ret = 0
    red_cap = 12
    green_cap = 13
    blue_cap = 14
    for l in data_lines:
        game_id, game_data = game_data_extractor(l)
        ret += math.prod(
            [
                max([d.red for d in game_data]),
                max([d.green for d in game_data]), 
                max([d.blue for d in game_data])
            ]
        )
    print(ret)
    
if __name__ == "__main__":
    solution_1()
    solution_2()