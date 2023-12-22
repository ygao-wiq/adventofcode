import collections
import utils


class Block:
    def __init__(self, identity: str, start_coord: tuple, end_coord: tuple):
        self.identity = identity
        self.start_coord = start_coord
        self.end_coord = end_coord

    def coordinates(self) -> list[tuple[int, int, int]]:
        return [self.start_coord, self.end_coord]

    def yz_placement(self) -> list[tuple[int, int]]:
        return [(y, z) for y in range(min(self.start_coord[1],self.end_coord[1]), max(self.start_coord[1],self.end_coord[1])+1) for z in range(min(self.start_coord[2], self.end_coord[2]), min(self.start_coord[2], self.end_coord[2])+ 1)]

    def xz_placement(self) -> list[tuple[int, int]]:
        return [(x, z) for x in range(min(self.start_coord[0], self.end_coord[0]), max(self.start_coord[0], self.end_coord[0]) + 1) for z in range(min(self.start_coord[2], self.end_coord[2]), min(self.start_coord[2], self.end_coord[2])+ 1)]

    def xy_placement(self) -> list[tuple[int, int]]:
        return [(x, y) for x in range(min(self.start_coord[0], self.end_coord[0]), max(self.start_coord[0], self.end_coord[0]) + 1) for y in range(min(self.start_coord[1],self.end_coord[1]), max(self.start_coord[1],self.end_coord[1])+1)]

    def xyz_placement(self) -> list[tuple[int, int, int]]:
        return [(x, y, z)
                for x in range(min(self.start_coord[0], self.end_coord[0]), max(self.start_coord[0], self.end_coord[0]) + 1)
                for y in range(min(self.start_coord[1], self.end_coord[1]), max(self.start_coord[1], self.end_coord[1]) + 1)
                # for z in range(min(self.start_coord[2], self.end_coord[2]), min(self.start_coord[2], self.end_coord[2])+ 1)
                for z in (self.start_coord[2], self.end_coord[2])
                ]

def convert_to_str(plot: list[list[str]]) -> str:
    ret = list()
    for line in plot:
        ret.append(",".join(line))
    return "\n".join(ret)

def solution_1(data_lines: list[str]):
    blocks = list()
    max_x = max_y = max_z = 0
    bricks = list()
    for idx, line in enumerate(data_lines):
        coordinates = tuple(map(lambda p: p.split(","), line.split("~")))
        start_coord, end_coord = tuple(map(int, coordinates[0])), tuple(map(int, coordinates[1]))
        blocks.append(Block(str(idx), start_coord, end_coord))
        bricks.append((min(start_coord[2], end_coord[2]), set(blocks[-1].xyz_placement())))
        max_x = max(max(max_x, end_coord[0]), start_coord[0])
        max_y = max(max(max_y, end_coord[1]), start_coord[1])
        max_z = max(max(max_z, end_coord[2]), start_coord[2])
    dimension = max(max_x, max_y, max_z)
    sorted_bricks = [b for z, b in sorted(bricks)]
    supporting_bricks = collections.defaultdict(set)
    supported_by = collections.defaultdict(set)
    settled_positions = {}
    highest_z_per_point = {}
    for idx, b in enumerate(sorted_bricks):
        delta_z = min(z-highest_z_per_point.get((x, y), 0)-1 for x, y, z in b)
        b = {(x, y, z-delta_z) for x, y, z in b}
        b_supporting = {(x, y, z-1) for x, y, z in b}
        for c in b_supporting:
            idx2 = settled_positions.get(c)
            if idx2 is not None:
                supporting_bricks[idx2].add(idx)
                supported_by[idx].add(idx2)
        for x, y, z in b:
            settled_positions[x, y, z] = idx
            highest_z_per_point[x, y] = max(z, highest_z_per_point.get((x,y), z))
        sorted_bricks[idx] = b
    ret = 0
    for brick in range(len(sorted_bricks)):
        if all(len(supported_by.get(supported, [])) != 1 for supported in supporting_bricks.get(brick, [])):
            # all() returns True for empty list
            ret += 1
    print(ret)

def solution_2(data_lines: list[str]):
    blocks = list()
    max_x = max_y = max_z = 0
    bricks = list()
    for idx, line in enumerate(data_lines):
        coordinates = tuple(map(lambda p: p.split(","), line.split("~")))
        start_coord, end_coord = tuple(map(int, coordinates[0])), tuple(map(int, coordinates[1]))
        blocks.append(Block(str(idx), start_coord, end_coord))
        bricks.append((min(start_coord[2], end_coord[2]), set(blocks[-1].xyz_placement())))
        max_x = max(max(max_x, end_coord[0]), start_coord[0])
        max_y = max(max(max_y, end_coord[1]), start_coord[1])
        max_z = max(max(max_z, end_coord[2]), start_coord[2])
    dimension = max(max_x, max_y, max_z)
    sorted_bricks = [b for z, b in sorted(bricks)]
    supporting_bricks = collections.defaultdict(set)
    supported_by = collections.defaultdict(set)
    settled_positions = {}
    highest_z_per_point = {}
    for idx, b in enumerate(sorted_bricks):
        delta_z = min(z-highest_z_per_point.get((x, y), 0)-1 for x, y, z in b)
        b = {(x, y, z-delta_z) for x, y, z in b}
        b_supporting = {(x, y, z-1) for x, y, z in b}
        for c in b_supporting:
            idx2 = settled_positions.get(c)
            if idx2 is not None:
                supporting_bricks[idx2].add(idx)
                supported_by[idx].add(idx2)
        for x, y, z in b:
            settled_positions[x, y, z] = idx
            highest_z_per_point[x, y] = max(z, highest_z_per_point.get((x,y), z))
        sorted_bricks[idx] = b
    ret = 0
    for brick in range(len(sorted_bricks)):
        supports_lost = {brick}
        todo = list(supporting_bricks.get(brick, []))
        while todo:
            b = todo.pop()
            if b in supports_lost:
                continue

            if all(supporting in supports_lost
                   for supporting in supported_by.get(b, [])):
                ret += 1
                supports_lost.add(b)
                todo.extend(supporting_bricks.get(b, []))
    print(ret)

if __name__ == "__main__":
    data_lines = utils.get_file_content("day22.dat")
    data_lines = [l.strip() for l in data_lines]
    solution_1(data_lines)
    solution_2(data_lines)