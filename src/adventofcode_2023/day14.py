import utils

def solution_1():
    data_lines = utils.get_file_content("day14.dat")
    data_lines = [l.strip() for l in data_lines]
    curr_weight = len(data_lines)
    current_nearest_squares = [-1 for i in range(len(data_lines[0]))]
    ret = 0
    for idx, l in enumerate(data_lines):
        for col, c in enumerate(l):
            if c == "O":
                if current_nearest_squares == -1:
                    ret += curr_weight - idx
                else:
                    ret += (curr_weight - current_nearest_squares[col] - 1)
                current_nearest_squares[col] = current_nearest_squares[col]+1
            elif c == "#":
                current_nearest_squares[col] = idx
    print(ret)


def calc_loads(data_lines: list[list[str]]) -> int:
    curr_weight = len(data_lines)
    ret = 0
    for idx, l in enumerate(data_lines):
        for col, c in enumerate(l):
            if c == "O":
                ret += curr_weight - idx
    return ret

def convert_to_str(data_lines: list[list[str]]) -> str:
    ret = list()
    for l in data_lines:
        ret.append("".join(l))
    return "\n".join(ret)

def tilt_helper(plot: list[list[str]]):
    # North
    for r in range(len(plot)):
        for c in range(len(plot[0])):
            spot = plot[r][c]
            if spot == 'O':
                temp_r = r
                while temp_r > 0:
                    if plot[temp_r-1][c] == '.':
                        temp_r -= 1
                    else:
                        break
                plot[r][c] = '.'
                plot[temp_r][c] = 'O'

    # West
    for r in range(len(plot)):
        for c in range(len(plot[0])):
            spot = plot[r][c]
            if spot == 'O':
                temp_c = c
                while temp_c > 0:
                    if plot[r][temp_c-1] == '.':
                        temp_c -= 1
                    else:
                        break
                plot[r][c] = '.'
                plot[r][temp_c] = 'O'

    # South
    for r in reversed(range(len(plot))):
        for c in range(len(plot[0])):
            spot = plot[r][c]
            if spot == 'O':
                temp_r = r
                while temp_r < len(plot)-1:
                    if plot[temp_r+1][c] == '.':
                        temp_r += 1
                    else:
                        break
                plot[r][c] = '.'
                plot[temp_r][c] = 'O'

    # East
    for r in range(len(plot)):
        for c in reversed(range(len(plot[0]))):
            spot = plot[r][c]
            if spot == 'O':
                temp_c = c
                while temp_c < len(plot[0])-1:
                    if plot[r][temp_c+1] == '.':
                        temp_c += 1
                    else:
                        break
                plot[r][c] = '.'
                plot[r][temp_c] = 'O'

def solution_2():
    data_lines = utils.get_file_content("day14.dat")
    data_lines = [l.strip() for l in data_lines]
    plot = list()
    for idx, l in enumerate(data_lines):
        if idx >= len(plot):
            plot.append(list())
            for c in l:
                plot[idx].append(c)
    plot_cache = dict()
    plot_cache[convert_to_str(plot)] = 0
    cycle = 0
    while cycle < 1000000000:
        cycle += 1
        tilt_helper(plot)
        if convert_to_str(plot) in plot_cache:
            delta = cycle - plot_cache[convert_to_str(plot)]
            rem = 1000000000 - cycle
            cycle_skipped = (rem // delta) * delta
            cycle += cycle_skipped
            break
        plot_cache[convert_to_str(plot)] = cycle
    while cycle < 1000000000:
        cycle += 1
        tilt_helper(plot)
    print(calc_loads(plot))


if __name__ == "__main__":
    solution_1()
    solution_2()