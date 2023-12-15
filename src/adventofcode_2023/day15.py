import utils


def my_hash(raw_str: str) -> int:
    ret = 0
    for c in raw_str:
        ret += ord(c)
        ret = ret * 17
        ret %= 256
    return ret
def solution_1():
    data_lines = utils.get_file_content("day15.dat")
    data_lines = [l.strip() for l in data_lines]
    ret = 0
    for l in data_lines:
        for step in l.split(","):
            ret +=my_hash(step.strip())
    print(ret)


def remove(box: list[tuple[str, int]], label_op):
    i = 0
    while i<len(box):
        if label_op[0] == box[i][0]:
            break
        i += 1
    if i<len(box):
        del box[i]

def update(box: list[tuple[str, int]], label_op):
    i = 0
    while i<len(box):
        if label_op[0] == box[i][0]:
            break
        i += 1
    if i<len(box):
        box[i]=(label_op[0], label_op[1])
    else:
        box.append((label_op[0], label_op[1]))

def solution_2():
    data_lines = utils.get_file_content("day15.dat")
    data_lines = [l.strip() for l in data_lines]
    boxes = list()
    boxes_qty = 256
    for _ in range(boxes_qty):
        boxes.append(list())
    ret = 0
    for l in data_lines:
        for step in l.split(","):
            if "-" in step:
                temp = step.split("-")
                step_hash = my_hash(temp[0])
                assert step_hash < 256
                box = boxes[step_hash]
                label_ops = (temp[0], -1)
                remove(box, label_ops)
            else:
                temp = step.split("=")
                step_hash = my_hash(temp[0])
                assert step_hash < 256
                box = boxes[step_hash]
                label_ops = (temp[0], int(temp[1]))
                update(box, label_ops)
    ret = 0
    for box_idx, box in enumerate(boxes):
        for slot_idx, focal_len in enumerate(box):
            ret += (1+box_idx)*(slot_idx+1)*int(focal_len[1])
    print(ret)


if __name__ == "__main__":
    solution_1()
    solution_2()