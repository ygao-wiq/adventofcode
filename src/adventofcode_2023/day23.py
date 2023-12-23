import utils

directions = {
    ">": [(1, 0)],
    "^": [(0, -1)],
    "<": [(-1, 0)],
    "v": [(0, 1)],
    ".": [(1, 0), (-1, 0), (0, -1), (0, 1)]
}

reversed_directions = {
    ">": (-1, 0),
    "^": (0, 1),
    "<": (1, 0),
    "v": (0, -1),
}


def next_possible_steps(walking_map: list[list[str]], start_coord: tuple[int, int]) -> list[tuple[int, int]]:
    ret = list()
    x, y = start_coord
    for dx, dy in directions[walking_map[y][x]]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(walking_map[0]) and 0 <= new_y < len(walking_map) and walking_map[new_y][new_x] != "#":
            ret.append((x + dx, y + dy))
    return ret


def next_possible_steps2(walking_map: list[list[str]], seen: set[tuple[int, int]], start_coord: tuple[int, int]) -> list[tuple[int, int]]:
    ret = list()
    x, y = start_coord
    for dx, dy in directions["."]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(walking_map[0]) and 0 <= new_y < len(walking_map) and (new_x, new_y) not in seen and walking_map[new_y][new_x] != "#":
            ret.append((x + dx, y + dy))
    return ret


def solve(walking_map: list[list[str]], seen: set[tuple[int, int]], start_coord: tuple[int, int],
          end_coord: tuple[int, int]) -> int:
    ret = 0
    if start_coord == end_coord:
        return ret
    seen.add(start_coord)
    for (new_x, new_y) in next_possible_steps(walking_map, start_coord):
        if (new_x, new_y) in seen:
            continue
        ret = max(ret, 1 + solve(walking_map, seen.copy(), (new_x, new_y), end_coord))
    return ret


def solution_1(data_lines: list[str]):
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    height = len(data_lines)
    width = len(data_lines[0])
    walking_map = [["" for _ in range(width)] for _ in range(height)]
    distance_map = [[-1 for _ in range(width)] for _ in range(height)]
    for y, line in enumerate(data_lines):
        for x, char in enumerate(line):
            walking_map[y][x] = char
            if char == ".":
                distance_map[y][x] = 0
                if y == 0:
                    start_x, start_y = x, y
                if y == height - 1:
                    end_x, end_y = x, y

    seen = set()
    ret = 0
    queue = [((start_x, start_y), 0, seen.copy())]
    while queue:
        (x, y), distance, visited = queue.pop(0)
        ret = max(ret, distance)
        visited.add((x, y))
        if (x, y) == (end_x, end_y):
            continue
        for (new_x, new_y) in next_possible_steps(walking_map, (x, y)):
            if (new_x, new_y) in visited:
                continue
            queue.append(((new_x, new_y), distance + 1, visited.copy()))
    # ret = max(ret, solve(walking_map, seen.copy(), (start_x, start_y), (end_x, end_y)))
    print(ret)


def solution_2(data_lines: list[str]):
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    height = len(data_lines)
    width = len(data_lines[0])
    walking_map = [["" for _ in range(width)] for _ in range(height)]
    distance_map = [[-1 for _ in range(width)] for _ in range(height)]
    for y, line in enumerate(data_lines):
        for x, char in enumerate(line):
            walking_map[y][x] = char
            if char == ".":
                distance_map[y][x] = 0
                if y == 0:
                    start_x, start_y = x, y
                if y == height - 1:
                    end_x, end_y = x, y

    seen = set()
    ret = 0
    queue = [((start_x, start_y), 0, seen.copy())]
    while queue:
        (x, y), distance, visited = queue.pop(0)
        visited.add((x, y))
        if (x, y) == (end_x, end_y):
            print(distance)
            ret = max(ret, distance)
            continue
        for (new_x, new_y) in next_possible_steps2(walking_map, visited, (x, y)):
            queue.append(((new_x, new_y), distance + 1, visited.copy()))
    # ret = max(ret, solve(walking_map, seen.copy(), (start_x, start_y), (end_x, end_y)))
    print(ret)


if __name__ == "__main__":
    data_lines = utils.get_file_content("day23.dat")
    data_lines = [l.strip() for l in data_lines]
    solution_1(data_lines)
    solution_2(data_lines)
