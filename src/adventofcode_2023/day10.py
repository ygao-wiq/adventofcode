import enum
import utils

class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class DirectionOffset(enum.Enum):
    UP = (0,-1)
    DOWN = (0,1)
    LEFT = (-1,0)
    RIGHT = (1,0)

connective_maps = {
    "|": {Direction.UP, Direction.DOWN},
    "-": {Direction.LEFT, Direction.RIGHT},
    "L": {Direction.UP, Direction.RIGHT},
    "J": {Direction.UP, Direction.LEFT},
    "7": {Direction.LEFT, Direction.DOWN},
    "F": {Direction.RIGHT, Direction.DOWN},
    ".": {},
}

opposite_connective_maps = {
    "|": {Direction.DOWN, Direction.UP},
    "-": {Direction.RIGHT, Direction.LEFT},
    "L": {Direction.DOWN, Direction.LEFT},
    "J": {Direction.DOWN, Direction.RIGHT},
    "7": {Direction.RIGHT, Direction.UP},
    "F": {Direction.LEFT, Direction.UP},
    ".": {},
}

direction_offsets = {
    Direction.UP: (0,-1),
    Direction.DOWN: (0,1),
    Direction.LEFT: (-1,0),
    Direction.RIGHT: (1,0),
}

def is_pipes_connected(src_pipe: str, dest_pipe: str, position: Direction) -> bool:
    if position in connective_maps[src_pipe]:
        return position in opposite_connective_maps[dest_pipe]
    return False

def find_connected_spots(start_coordiates: (int, int), chart_map: list[list[str]], distance_map: list[list[int]]) -> list[(int, int)]:
    src_x = start_coordiates[0]
    src_y = start_coordiates[1]
    ret = []
    for direction in [Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT]:
        offsets = direction_offsets[direction]
        dest_x = src_x + offsets[0]
        dest_y = src_y + offsets[1]
        if dest_y >= len(chart_map) or dest_y < 0 or dest_x >= len(chart_map[0]) or dest_x < 0:
            continue
        if is_pipes_connected(chart_map[src_y][src_x], chart_map[dest_y][dest_x], direction):
           ret.append((dest_x, dest_y)) 
    return ret
    
def solution_1():
    start_x, start_y = 0, 0
    farest_distance = 0
    data_lines = utils.get_file_content("day10.dat")
    chart_map = []
    distance_map = []
    for y, line in enumerate(data_lines):
        chart_map.append(list())
        distance_map.append(list())
        for x, spot in enumerate(line.strip()):
            if spot == "S":
                start_x = x
                start_y = y
                chart_map[y].append("F") # trick here; sample with F and puzzle with L
            else:
                chart_map[y].append(spot)
            distance_map[y].append(-1)
    distance_map[start_y][start_x] = 0
    queue = [(start_x, start_y)]
    
    while len(queue) > 0:
        s = queue.pop(0)
        curr_distance = distance_map[s[1]][s[0]]
        neighbours = find_connected_spots(s, chart_map, distance_map)
        for n in neighbours:
            if distance_map[n[1]][n[0]] == -1:
                distance_map[n[1]][n[0]] = curr_distance + 1
                queue.append((n[0], n[1]))
                farest_distance = max(farest_distance, curr_distance+1)
    print(farest_distance)
    

def solution_2():
    data_lines = utils.get_file_content("day10_sample.dat")
    start_x, start_y = 0, 0
    farest_distance = 0
    data_lines = utils.get_file_content("day10.dat")
    chart_map = []
    distance_map = []
    for y, line in enumerate(data_lines):
        chart_map.append(list())
        distance_map.append(list())
        for x, spot in enumerate(line.strip()):
            if spot == "S":
                start_x = x
                start_y = y
                chart_map[y].append("L") # trick here; sample with F and puzzle with L
            else:
                chart_map[y].append(spot)
            distance_map[y].append(-1)
    distance_map[start_y][start_x] = 0
    queue = [(start_x, start_y)]
    seen = set()
    edges = []
    
    while len(queue) > 0:
        seen.update(queue)
        next_queue = set()
        for spot in queue:
            c = chart_map[spot[1]][spot[0]]
            neightbours = find_connected_spots(spot, chart_map, distance_map)
            for n in neightbours:
                if n in seen:
                    continue
                next_queue.add(n)
                edges.append(((spot[0],spot[1]),n))
        queue = list(next_queue)

    loop = set()
    for (x, y), (x2, y2) in edges:
        loop.add((2*x,2*y))
        loop.add((2*x2,2*y2))
        loop.add((x+x2,y+y2))

    handled = set(loop)

    contained = set()
    items = []
    for y, row in enumerate(chart_map):
        for x, _ in enumerate(row):
            items.append((x*2,y*2))
    for (x,y) in items:
        if (x,y) in handled:
            continue
        expanded = {(x,y)}
        to_handle = [(x,y)]
        escaped = False

        while to_handle:
            x,y = to_handle.pop(0)

            for nx,ny in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
                if nx < 0 or nx > (len(chart_map[0]) * 2) - 2:
                    escaped = True
                    continue
                if ny < 0 or ny > (len(chart_map) * 2) - 2:
                    escaped = True
                    continue
                if (nx,ny) in handled:
                    continue
                if (nx,ny) in expanded:
                    continue
                to_handle.append((nx,ny))
                expanded.add((nx,ny))
        handled.update(expanded)
        if not escaped:
            contained.update(expanded)

    print(len([(x//2,y//2) for x,y in contained if x % 2 == 0 and y % 2 == 0]))
    
if __name__ == "__main__":
    solution_1()
    solution_2()
