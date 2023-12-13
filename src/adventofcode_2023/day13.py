import copy
import utils

def is_vertical_mirrored(line: str, first_start: int, second_start: int) -> bool:
    while first_start>=0 and second_start<=len(line)-1:
        if line[first_start] != line[second_start]:
            return False
        first_start -= 1
        second_start += 1
    return True

def is_horizontal_mirrored(lines: list[str], first_start: int, second_start: int) -> bool:
    while first_start>=0 and second_start<=len(lines)-1:
        if lines[first_start] != lines[second_start]:
            return False
        first_start -= 1
        second_start += 1
    return True


def calc_patterns(lines: list[str]) -> int:
    ret = 0
    i = 0
    while i <= len(lines)-2:
        if is_horizontal_mirrored(lines, i, i+1):
            return (i+1)*100
        i += 1
    i = 0
    while i <= len(lines[0]) - 2:
        found_vertical_mirror = True
        for line in lines:
            if not is_vertical_mirrored(line, i, i+1):
                found_vertical_mirror = False
                break
        i += 1
        if found_vertical_mirror:
            return i
    return ret

def calc_patterns2(lines: list[str], excluded: int) -> int:
    ret = 0
    i = 0
    while i <= len(lines)-2:
        if is_horizontal_mirrored(lines, i, i+1) and (i+1)*100 != excluded:
            return (i+1)*100
        i += 1
    i = 0
    while i <= len(lines[0]) - 2:
        found_vertical_mirror = True
        for line in lines:
            if not is_vertical_mirrored(line, i, i+1):
                found_vertical_mirror = False
                break
        i += 1
        if found_vertical_mirror and i != excluded:
            return i
    return ret

def mutate_lines(lines: list[str]) -> list[str]:
    i = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            old = lines[i]
            if lines[i][j] == ".":
                replacement = "#"
            else:
                replacement = "."
            lines[i] = lines[i][:j] + replacement + lines[i][j + 1:]
            yield lines, i, j
            j += 1
            lines[i] = old
        i += 1
def solution_1():
    data_lines = utils.get_file_content("day13.dat")
    data_lines = [line.strip() for line in data_lines]
    i = 0
    last_start = 0
    groups = list()
    while i < len(data_lines):
        if len(data_lines[i]) == 0:
            groups.append(data_lines[last_start:i])
            last_start = i+1
        i += 1
    if last_start < i:
        groups.append(data_lines[last_start:])
    ret = 0
    for lines in groups:
        ret += calc_patterns(lines)
    print(ret)

def solution_2():
    data_lines = utils.get_file_content("day13.dat")
    data_lines = [line.strip() for line in data_lines]
    i = 0
    last_start = 0
    groups = list()
    while i < len(data_lines):
        if len(data_lines[i]) == 0:
            groups.append(data_lines[last_start:i])
            last_start = i+1
        i += 1
    if last_start < i:
        groups.append(data_lines[last_start:])
    ret = 0

    for idx, lines in enumerate(groups):
        temp_lines = copy.deepcopy(lines)
        temp_original = calc_patterns(lines)
        for mutated, i, j in mutate_lines(temp_lines):
            temp_mutated  = calc_patterns2(mutated, temp_original)
            if temp_mutated > 0 and temp_original != temp_mutated:
                ret += temp_mutated
                break
    print(ret)


if __name__ == "__main__":
    solution_1()
    solution_2()