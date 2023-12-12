import utils

def is_valid(row: str,  broken_array: list[int]) -> bool:
    broken_onsens = [r for r in row.split(".") if len(r)>0]
    if len(broken_onsens) == len(broken_array) and all([len(r)==int(broken_array[i]) for i, r in enumerate(broken_onsens)]):
        return True
    return False

def solve_1(row: str, broken_array: list[int], start_idx: int) -> int:
    ret = 0
    if start_idx >= len(row):
        if is_valid(row, broken_array):
            return 1
        else:
            return 0
    elif row[start_idx] != "?":
        return solve_1(row, broken_array.copy(), start_idx+1)
    else:
        new_row = row[:start_idx] + "." + row[start_idx+1:]
        ret += solve_1(new_row, broken_array.copy(), start_idx+1)
        new_row = row[:start_idx] + "#" + row[start_idx+1:]
        ret += solve_1(new_row, broken_array.copy(), start_idx+1)
    return ret
def solution_1():
    data_lines = utils.get_file_content("day12.dat")
    ret = 0

    for line in data_lines:
        line = line.strip()
        onsen_lst = line.split(" ")[0]
        broken_array = line.split(" ")[1].split(",")
        ret += solve_1(onsen_lst, broken_array, 0)
    print(ret)

solve2_ret_cache = dict()
def solve_2(onsens, numbers):
    if (onsens, numbers) in solve2_ret_cache:
        return solve2_ret_cache[(onsens, numbers)]
    size = len(onsens)
    if len(numbers) == 0:
        if all(c in '.?' for c in onsens):
            return 1
        return 0
    first_brokens = numbers[0]
    remained_numbers = numbers[1:]
    remained_onsens_qty = sum(remained_numbers) + len(remained_numbers)
    count = 0
    for i in range(size-remained_onsens_qty-first_brokens+1):
        candidate = '.' * i + '#' * first_brokens + '.'
        j = 0
        valid = True
        while j < min(len(onsens), len(candidate)):
            if onsens[j] != "?" and onsens[j] != candidate[j]:
                valid = False
                break
            j += 1
        if valid:
            solve2_ret_cache[(onsens[len(candidate):], remained_numbers)] = solve_2(onsens[len(candidate):], remained_numbers)
            count += solve2_ret_cache[(onsens[len(candidate):], remained_numbers)]
    return count
def solution_2():
    data_lines = utils.get_file_content("day12.dat")
    ret = 0
    for line in data_lines:
        line = line.strip()
        onsens, numbers = line.split()
        onsens = '?'.join((onsens,) * 5)
        numbers = tuple([int(n) for n in numbers.split(',')]) * 5
        ret += solve_2(onsens, numbers)
    print(ret)

if __name__ == "__main__":
    solution_1()
    solution_2()


