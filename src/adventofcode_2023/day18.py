import utils

direct_offset = {
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0)
}

direct_offset2 = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def convert_to_str(digging_map):
    temp = ["".join(l) for l in digging_map]
    return "\n".join(temp)

def calc_area(lines):
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0.0
    for i in range(len(lines)):
        j = (i + 1) % len(lines)
        area = area + lines[i][0] * lines[j][1] - lines[j][0] * lines[i][1]
    area = abs(area) / 2.0
    return area
def solution_1():
    data_lines = utils.get_file_content("day18.dat")
    data_lines = [r.strip() for r in data_lines]
    start_spot = (0, 0)
    hit_spots = [start_spot]
    hit_lines = [start_spot]
    lines_spots_qty = 0
    for line in data_lines:
        direction, steps, color = line.split(" ")
        steps = int(steps)
        for _ in range(steps):
            start_spot = (start_spot[0] + direct_offset[direction][0], start_spot[1] + direct_offset[direction][1])
            hit_spots.append(start_spot)
        hit_lines.append(start_spot)
        lines_spots_qty += steps
    min_y = min([p[1] for p in hit_spots])
    max_y = max([p[1] for p in hit_spots])
    min_x = min([p[0] for p in hit_spots])
    max_x = max([p[0] for p in hit_spots])
    height = max_y - min_y + 1
    width = max_x - min_x + 1
    digging_map = [["."]*width for _ in range(height)]
    for spot in hit_spots:
        digging_map[spot[1]-min_y][spot[0]-min_x] = "#"
    print(convert_to_str(digging_map))
    print(calc_area(hit_lines)+lines_spots_qty // 2 + 1)

def solution_2():
    data_lines = utils.get_file_content("day18.dat")
    data_lines = [r.strip() for r in data_lines]
    start_spot = (0, 0)
    hit_lines = [start_spot]
    lines_spots_qty = 0
    for line in data_lines:
        code = line.split(" ")[2][2:-1]
        steps = int(code[:-1], 16)
        direction = int(code[-1])
        start_spot = (start_spot[0] + direct_offset2[direction][0]*steps, start_spot[1] + direct_offset2[direction][1]*steps)
        hit_lines.append(start_spot)
        lines_spots_qty += steps
    print(calc_area(hit_lines)+lines_spots_qty // 2 + 1)


if __name__ == "__main__":
    solution_1()
    solution_2()