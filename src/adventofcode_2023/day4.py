import utils

def solution_1():
    data_lines = [l.strip() for l in utils.get_file_content("day4.dat")]
    ret = 0
    for line in data_lines:
        raw_data_part = line.split(":")[1].strip()
        data = [[int(e.strip()) for e in r.strip().split(" ") if len(e)>0] for r in raw_data_part.split("|")]
        winning_set = set(data[0])
        competing_set = set(data[1])
        result = winning_set & competing_set
        if len(result) > 0:
            ret += 2 ** (len(result)-1)
    print(ret)

def solution_2():
    data_lines = [l.strip() for l in utils.get_file_content("day4.dat")]
    ret = 0
    original_cards = dict()
    total_held_cards = dict()
    for idx, line in enumerate(data_lines):
        raw_data_part = line.split(":")[1].strip()
        data = [[int(e.strip()) for e in r.strip().split(" ") if len(e)>0] for r in raw_data_part.split("|")]
        original_cards[idx] = data
        total_held_cards[idx] = 1
    total_cards_qty = len(original_cards)
    i = 0
    while i < total_cards_qty:
        data = original_cards[i]
        winning_set = set(data[0])
        competing_set = set(data[1])
        result = winning_set & competing_set
        if len(result) > 0:
            for copy_idx in range(i+1, min(i+len(result)+1, total_cards_qty)):
                total_held_cards[copy_idx] += total_held_cards[i]
        i += 1
    for v in total_held_cards.values():
        ret += v
    print(ret)


if __name__ == "__main__":
    solution_1()
    solution_2()