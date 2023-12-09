import utils


def extrapolate_history_tail(line: str) -> int:
    initial_data_points = [int(e) for e in line.split()]
    curr = initial_data_points
    history = list()
    while len(curr) > 0:
        history.append(curr.copy())
        diff = list(map(lambda x: x[1]-x[0], zip(curr[:-1], curr[1:])))
        if any(diff):
            curr = diff
            continue
        else:
            break
    ret = 0
    i = len(history)-1
    while i>=0:
        ret += history[i][-1]
        i -= 1
    return ret
def solution_1():
    data_lines = utils.get_file_content("day9.dat")
    ret = list()
    for line in data_lines:
        ret.append(extrapolate_history_tail(line.strip()))
    print(sum(ret))
    
def extrapolate_history_head(line: str) -> int:
    initial_data_points = [int(e) for e in line.split()]
    curr = initial_data_points
    history = list()
    while len(curr) > 0:
        history.append(curr.copy())
        diff = list(map(lambda x: x[1]-x[0], zip(curr[:-1], curr[1:])))
        if any(diff):
            curr = diff
            continue
        else:
            break
    ret = 0
    i = len(history)-1
    while i>=0:
        ret = history[i][0] - ret
        i -= 1
    return ret

def solution_2():
    data_lines = utils.get_file_content("day9.dat")
    ret = list()
    for line in data_lines:
        ret.append(extrapolate_history_head(line.strip()))
    print(sum(ret))
    
if __name__ == "__main__":
    solution_1()
    solution_2()