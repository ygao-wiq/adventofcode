import enum
import utils

class Direction(enum.Enum):
    LEFT = (-1, 0)
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)

symbols_direction = {
    Direction.LEFT: "<",
    Direction.UP: "^",
    Direction.RIGHT: ">",
    Direction.DOWN: "v"
}

def solution_1_movement_heler(x: int, y: int, direction: Direction, plot: list[str]) -> list[(int, int, Direction)]:
    spot = plot[y][x]
    if spot == ".":
        next_direction = direction
        direction_offset = next_direction.value
        return [(x + direction_offset[0], y + direction_offset[1], next_direction)]
    elif spot == "/":
        if direction == Direction.LEFT:
            next_direction = Direction.DOWN
        elif direction == Direction.UP:
            next_direction = Direction.RIGHT
        elif direction == Direction.RIGHT:
            next_direction = Direction.UP
        elif direction == Direction.DOWN:
            next_direction = Direction.LEFT
        direction_offset = next_direction.value
        return [(x + direction_offset[0], y + direction_offset[1], next_direction)]
    elif spot == "\\":
        if direction == Direction.LEFT:
            next_direction = Direction.UP
        elif direction == Direction.UP:
            next_direction = Direction.LEFT
        elif direction == Direction.RIGHT:
            next_direction = Direction.DOWN
        elif direction == Direction.DOWN:
            next_direction = Direction.RIGHT
        direction_offset = next_direction.value
        return [(x + direction_offset[0], y + direction_offset[1], next_direction)]
    elif spot == "|":
        if direction == Direction.UP or direction == Direction.DOWN:
            next_direction = direction
            direction_offset = next_direction.value
            return [(x + direction_offset[0], y + direction_offset[1], next_direction)]
        elif direction == Direction.LEFT or direction == Direction.RIGHT:
            return [(x, y - 1, Direction.UP), (x, y + 1, Direction.DOWN)]
    elif spot == "-":
        if direction == Direction.LEFT or direction == Direction.RIGHT:
            next_direction = direction
            direction_offset = next_direction.value
            return [(x + direction_offset[0], y + direction_offset[1], next_direction)]
        elif direction == Direction.UP or direction == Direction.DOWN:
            return [(x-1, y, Direction.LEFT), (x+1, y, Direction.RIGHT)]
    else:
        assert False, "Invalid"

def solution_1(init_x, init_y, init_direction):
    data_lines = utils.get_file_content("day16.dat")
    data_lines = [r.strip() for r in data_lines]
    queue = list()
    height = len(data_lines)
    width = len(data_lines[0])
    energized = [["."]*width for _ in range(height)]
    seen = [[""]*width for _ in range(height)]
    queue.append((init_x, init_y, init_direction))
    while queue:
        (x, y, direction) = queue.pop(0)
        while True:
            if energized[y][x] == ".":
                energized[y][x] = "#"
            if symbols_direction[direction] not in seen[y][x]:
                seen[y][x] += symbols_direction[direction]
            else:
                break
            if x == 6 and y == 6:
                pass
            next_movements = solution_1_movement_heler(x, y, direction, data_lines)
            if len(next_movements)>1:
                next_x, next_y, next_direction = next_movements[1]
                if 0<=next_x<=width-1 and 0<=next_y<=height-1:
                    queue.append(next_movements[1])
            next_x, next_y, next_direction = next_movements[0]
            if next_x<0 or next_x>width-1 or next_y<0 or next_y>height-1:
                break
            x = next_x
            y = next_y
            direction = next_direction
    ret = 0
    for y in range(height):
        for x in range(width):
            if energized[y][x] == "#":
                ret += 1
    return(ret)

def solution_2():
    data_lines = utils.get_file_content("day16.dat")
    data_lines = [r.strip() for r in data_lines]
    height = len(data_lines)
    width = len(data_lines[0])
    points = [(x, y) for x in range(len(data_lines[0])) for y in range(len(data_lines))]
    points = [(x, y) for x, y in points if x==0 or y==0 or x==width-1 or y==height-1]
    ret = 0
    for init_x, init_y in points:
        directions = list()
        if init_y == 0:
            directions.append(Direction.DOWN)
        elif init_y == height-1:
            directions.append(Direction.UP)
        if init_x == width-1:
            directions.append(Direction.LEFT)
        elif init_x == 0:
            directions.append(Direction.RIGHT)
        for direction in directions:
            ret = max(ret, solution_1(init_x, init_y, direction))
    print(ret)



if __name__ == "__main__":
    print(solution_1(0, 0, Direction.RIGHT))
    solution_2()