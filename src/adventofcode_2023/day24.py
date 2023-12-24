import dataclasses
import utils
from z3 import *
@dataclasses.dataclass
class Hailstone:
    px: int
    py: int
    pz: int
    vx: int
    vy: int
    vz: int

def is_colliding_xy(hailstone1: Hailstone, hailstone2: Hailstone, max_x: int, max_y: int) -> bool:
    if (hailstone2.px-hailstone1.px)*(hailstone1.vy-hailstone2.vy) == (hailstone2.py-hailstone1.py)*(hailstone1.vx-hailstone2.vx):
        return 0<=hailstone1.px+hailstone1.vx*(hailstone2.px-hailstone1.px)/(hailstone1.vx-hailstone2.vx)<=max_x and 0<=hailstone1.py+hailstone1.vy*(hailstone2.py-hailstone1.py)/(hailstone1.vy-hailstone2.vy)<=max_y
    
    return False

def is_intersecting_xy(hailstone1: Hailstone, hailstone2: Hailstone, min_c: int, max_c: int) -> bool:
    #if abs(hailstone1.vy*hailstone2.vx) != abs(hailstone2.vy*hailstone1.vx):
    if (hailstone1.vy*hailstone2.vx - hailstone2.vy*hailstone1.vx) != 0:
        slope1 = hailstone1.vy / hailstone1.vx
        slope2 = hailstone2.vy / hailstone2.vx
        inter_x = (hailstone2.py-slope2*hailstone2.px-hailstone1.py+slope1*hailstone1.px)*(hailstone1.vx*hailstone2.vx)/(hailstone1.vy*hailstone2.vx-hailstone2.vy*hailstone1.vx)
        inter_y = (hailstone1.vy/hailstone1.vx)*inter_x+hailstone1.py-slope1*hailstone1.px
        valid_a = ((inter_x-hailstone1.px)>0)==(hailstone1.vx>0)
        valid_b = ((inter_x-hailstone2.px)>0)==(hailstone2.vx>0)
        return min_c<=inter_x<=max_c and min_c<=inter_y<=max_c and valid_a and valid_b
    return False

def solution_1(data_lines: list[str]):
    hailstones = list()
    min_c = 200000000000000
    max_c = 400000000000000
    # min_c = 7
    # max_c = 27
    for line in data_lines:
        (px, py, pz), (vx, vy, vz) = tuple(map(lambda p: p.split(", "), line.split(" @ ")))
        hailstones.append(Hailstone(int(px.strip()), int(py.strip()), int(pz.strip()), int(vx.strip()), int(vy.strip()), int(vz.strip())))
    ret = list()
    for i, hailstone1 in enumerate(hailstones):
        j = i+1
        while j<len(hailstones):
            hailstone2 = hailstones[j]
            if is_intersecting_xy(hailstone1, hailstone2, min_c, max_c):
                ret.append((i, j))
            j += 1
    print(len(ret))


def solution_2(data_lines: list[str]):
    hailstones = list()
    min_c = 200000000000000
    max_c = 400000000000000
    # min_c = 7
    # max_c = 27
    for line in data_lines:
        (px, py, pz), (vx, vy, vz) = tuple(map(lambda p: p.split(", "), line.split(" @ ")))
        hailstones.append(Hailstone(int(px.strip()), int(py.strip()), int(pz.strip()), int(vx.strip()), int(vy.strip()), int(vz.strip())))
    x,y,z,vx,vy,vz = Int('x'),Int('y'),Int('z'),Int('vx'),Int('vy'),Int('vz')
    T = [Int(f'T{i}') for i in range(len(hailstones))]
    SOLVE = Solver()
    for i in range(len(hailstones)):
        SOLVE.add(x + T[i]*vx - hailstones[i].px - T[i]*hailstones[i].vx == 0)
        SOLVE.add(y + T[i]*vy - hailstones[i].py - T[i]*hailstones[i].vy == 0)
        SOLVE.add(z + T[i]*vz - hailstones[i].pz - T[i]*hailstones[i].vz == 0)
    res = SOLVE.check()
    M = SOLVE.model()
    print(M.eval(x+y+z))

if __name__ == "__main__":
    data_lines = utils.get_file_content("day24.dat")
    data_lines = [l.strip() for l in data_lines]
    solution_1(data_lines)
    solution_2(data_lines)
