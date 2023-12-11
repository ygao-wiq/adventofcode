import math
import utils



def solution_1():
    data_lines = utils.get_file_content("day11.dat")
    galaxies_map = list()
    empty_columns = set()
    galaxies_coords = list()
    height = len(data_lines)
    width = len(data_lines[0].strip())
    x = 0
    while x<width:
        y = 0
        found_galaxy = False
        while y<height:
            if data_lines[y][x] == "#":
                found_galaxy = True
                break
            y += 1
        if not found_galaxy:
            empty_columns.add(x)
        x += 1
    x = 0
    y = 0
    mx = 0
    my = 0
    while y<height:
        galaxies_map.append(list())
        found_galaxy = False
        mx = 0
        x = 0
        while x<width:
            galaxies_map[my].append(data_lines[y][x])    
            if not found_galaxy and data_lines[y][x] == "#":
                found_galaxy = True
            if x in empty_columns:
                galaxies_map[my].append(".")
                mx += 2
            else:
                mx += 1
            x += 1
        if not found_galaxy:
            galaxies_map.append(["." for i in galaxies_map[-1]])
            my += 2
        else:
            my += 1
        y += 1
    
    height = len(galaxies_map)
    width = len(galaxies_map[0])
    x = 0
    y = 0
    while y<height:
        x = 0
        while x<width:
            if galaxies_map[y][x] == "#":
                galaxies_coords.append((x,y))
            x += 1
        y += 1
    i = 0
    ret = 0
    while i<len(galaxies_coords):
        j = i+1
        while j<len(galaxies_coords):
            ret += abs(galaxies_coords[i][0]-galaxies_coords[j][0])+abs(galaxies_coords[i][1]-galaxies_coords[j][1])
            j += 1
        i += 1
    print(ret)


def solution_2():
    data_lines = utils.get_file_content("day11.dat")
    galaxies_map = list()
    empty_columns = set()
    empty_rows = set()
    galaxies_coords = list()
    height = len(data_lines)
    width = len(data_lines[0].strip())
    x = 0
    while x<width:
        y = 0
        found_galaxy = False
        while y<height:
            if data_lines[y][x] == "#":
                found_galaxy = True
                break
            y += 1
        if not found_galaxy:
            empty_columns.add(x)
        x += 1
    x = 0
    y = 0
    while y<height:
        galaxies_map.append(list())
        found_galaxy = False
        x = 0
        while x<width:
            galaxies_map[y].append(data_lines[y][x])    
            if not found_galaxy and data_lines[y][x] == "#":
                found_galaxy = True
            x += 1
        if not found_galaxy:
            empty_rows.add(y)
        y += 1
    
    height = len(galaxies_map)
    width = len(galaxies_map[0])
    x = 0
    y = 0
    while y<height:
        x = 0
        while x<width:
            if galaxies_map[y][x] == "#":
                galaxies_coords.append((x,y))
            x += 1
        y += 1
    i = 0
    ret = 0
    while i<len(galaxies_coords):
        j = i+1
        while j<len(galaxies_coords):
            x_min = min(galaxies_coords[i][0],galaxies_coords[j][0])
            x_max = max(galaxies_coords[i][0],galaxies_coords[j][0])
            y_min = min(galaxies_coords[i][1],galaxies_coords[j][1])
            y_max = max(galaxies_coords[i][1],galaxies_coords[j][1])
            empty_columns_qty = len([c for c in empty_columns if x_min < c < x_max])
            empty_rows_qty = len([r for r in empty_rows if y_min < r < y_max])
            ret += abs(galaxies_coords[i][0]-galaxies_coords[j][0])+abs(galaxies_coords[i][1]-galaxies_coords[j][1]) + (1000000-1)*empty_columns_qty + (1000000-1)*empty_rows_qty
            j += 1
        i += 1
    print(ret)    
    
if __name__ == "__main__":
    solution_1()
    solution_2()