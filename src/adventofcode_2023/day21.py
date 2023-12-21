from collections import deque
import utils


def solution_1(data_lines: list[str]):
    height = len(data_lines)
    width = len(data_lines[0])
    garden_map = [["*" * width for _ in range(width)] for _ in range(height)]
    start_x, start_y = 0, 0
    for y, line in enumerate(data_lines):
        for x, char in enumerate(line):
            if char == "S":
                start_x, start_y = x, y
                char = "."
            garden_map[y][x] = char
    reachable = [(start_x, start_y)]
    for i in range(64):
        next_reachable = set()
        for s in reachable:
            candidates = [(s[0] + dx, s[1] + dy) for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1))]
            next_reachable.update(
                filter(lambda c: 0 <= c[0] < width and 0 <= c[1] < height and garden_map[c[1]][c[0]] != "#",
                       candidates))
        reachable = next_reachable
    print(len(reachable))


memorized_found = {}


def find_others(distance, mode, target_steps, height):
    folds = (target_steps - distance) // height
    if (distance, mode, target_steps) in memorized_found:
        return memorized_found[(distance, mode, target_steps)]
    ret = 0
    for x in range(1, folds + 1):
        if (distance + height * x) <= target_steps and (distance + height * x) % 2 == (target_steps % 2):
            ret += ((x + 1) if mode == 2 else 1)  # 1 -- edge replica; 2 -- corner replica
    memorized_found[(distance, mode, target_steps)] = ret
    return ret


def solution_2(data_lines: list[str]):
    height = len(data_lines)
    width = len(data_lines[0])
    garden_map = [["*" * width for _ in range(width)] for _ in range(height)]
    start_x, start_y = 0, 0
    for y, line in enumerate(data_lines):
        for x, char in enumerate(line):
            if char == "S":
                start_x, start_y = x, y
                char = "."
            garden_map[y][x] = char

    distances = {}
    queue = [(start_x, start_y, 0, 0, 0)]
    while queue:
        s = queue.pop(0)
        if not garden_map[s[1]][s[0]] != '#':
            continue
        if (s[3], s[2], s[1], s[0]) in distances:
            continue
        if abs(s[2]) > 4 or abs(s[3]) > 4:
            continue
        distances[(s[3], s[2], s[1], s[0])] = s[4]
        candidates = [((s[0] + dx) % width, (s[1] + dy) % height, s[2] + (s[0] + dx) // width,
                       s[3] + (s[1] + dy) // height, s[4] + 1) for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1))]
        # candidates = [((s[0] + dx), (s[1] + dy), s[2], s[3], s[4] + 1) for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1))]
        queue.extend(candidates)

    ret = 0
    for y in range(height):
        for x in range(width):
            if (0, 0, y, x) in distances:
                available_replicas = [-3, -2, -1, 0, 1, 2, 3]
                for replica_y in available_replicas:
                    for replica_x in available_replicas:
                        d = distances[(replica_y, replica_x, y, x)]
                        if d % 2 == 26501365 % 2 and d <= 26501365:
                            ret += 1
                        if replica_y in [min(available_replicas), max(available_replicas)] and replica_x in [
                            min(available_replicas), max(available_replicas)]:
                            ret += find_others(d, 2, 26501365, height)
                        elif replica_y in [min(available_replicas), max(available_replicas)] or replica_x in [
                            min(available_replicas), max(available_replicas)]:
                            ret += find_others(d, 1, 26501365, height)
    print(ret)


if __name__ == "__main__":
    data_lines = utils.get_file_content("day21.dat")
    data_lines = [l.strip() for l in data_lines]
    # solution_1(data_lines)
    solution_2(data_lines)
