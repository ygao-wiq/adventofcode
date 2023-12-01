import utils

def solution_1():
    data = utils.get_file_content("day1_1.dat")
    ret = 0
    for l in data:
        first = -1
        first_idx = -1
        last = -1
        for i, c in enumerate(l):
            if c.isdigit():
               if first == -1:
                   first = int(c)
                   first_idx = i
                   break
        for c in reversed(l[first_idx:]):
            if c.isdigit():
               if last == -1:
                   last = int(c)
                   break
        ret += first * 10 + last
    print(ret)

def solution_2():
    digit_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    reversed_digit_map = {
        "eno": 1,
        "owt": 2,
        "eerht": 3,
        "ruof": 4,
        "evif": 5,
        "xis": 6,
        "neves": 7,
        "thgie": 8,
        "enin": 9,
    }
    def helper(s: str, reverse=False):
        if not reverse:
            for key in digit_map:
                if s.startswith(key):
                    return key
            return None
        else:
            for key in reversed_digit_map:
                if s.startswith(key):
                    return key
            return None
    data = utils.get_file_content("day1_2.dat")
    ret = 0
    for l in data:
        first = -1
        last = -1
        i = 0
        first_idx = -1
        while i < len(l):
            num = -1
            if l[i].isdigit():
                num = int(l[i])
            else:
                num_key = helper(l[i:])
                if num_key:
                    num = digit_map[num_key]
            if num != -1:
                if first == -1:
                    first = num
                    first_idx = i
                    break
            i += 1
        r = "".join(reversed(l[first_idx:]))
        i = 0
        while i < len(r):
            num = -1
            if r[i].isdigit():
                num = int(r[i])
            else:
                num_key = helper(r[i:], reverse=True)
                if num_key:
                    num = reversed_digit_map[num_key]
            if num != -1:
                if last == -1:
                    last = num
                    break
            i += 1
        ret += first * 10 + last
    print(ret)
    
if __name__ == "__main__":
    solution_1()
    solution_2()