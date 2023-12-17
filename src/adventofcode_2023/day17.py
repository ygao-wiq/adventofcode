import heapq
import sys
import utils

def solution_1():
    data_lines = utils.get_file_content("day17.dat")
    data_lines = [r.strip() for r in data_lines]
    city_map = list()
    heat_loss_map = list()
    seen = set()
    height = len(data_lines)
    width = len(data_lines[0])
    for y in range(height):
        for x in range(width):
            if y >= len(city_map):
                city_map.append(list())
                heat_loss_map.append(list())
            city_map[y].append(int(data_lines[y][x]))
            heat_loss_map[y].append(sys.maxsize)
    heat_loss_map[height-1][width-1] = 0
    def graph_fn(state):
        x, y, dx, dy, same_directions = state
        for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            new_dx = new_x - x
            new_dy = new_y - y
            if new_dx == dx and new_dy == dy:
                if same_directions == 3:
                    continue
                new_same_directions = same_directions + 1
            elif new_dx == -dx and new_dx != 0:
                continue
            elif new_dy == -dy and new_dy != 0:
                continue
            else:
                new_same_directions = 1
            if 0 <= new_x < width and 0 <= new_y < height:
                new_state = (new_x, new_y, new_dx, new_dy, new_same_directions)
                yield new_state, city_map[new_y][new_x]
    ret = 0
    graph = utils.make_graph(graph_fn)
    queue = list()
    heapq.heapify(queue)
    heapq.heappush(queue, (0, (0, 0, -1, 0, 0)))
    while queue:
        curr_loss, current_node = heapq.heappop(queue)
        x, y = current_node[0], current_node[1]
        heat_loss_map[y][x] = curr_loss
        if current_node in seen:
            continue
        seen.add(current_node)
        if x == width - 1 and y == height - 1:
            ret = curr_loss
            break
        for neighbour_node, neighbour_loss in graph[current_node]:
            if neighbour_node in seen:
                continue
            heapq.heappush(queue, (curr_loss+neighbour_loss, neighbour_node))
    print(ret)

def solution_2():
    data_lines = utils.get_file_content("day17.dat")
    data_lines = [r.strip() for r in data_lines]
    city_map = list()
    heat_loss_map = list()
    seen = set()
    height = len(data_lines)
    width = len(data_lines[0])
    for y in range(height):
        for x in range(width):
            if y >= len(city_map):
                city_map.append(list())
                heat_loss_map.append(list())
            city_map[y].append(int(data_lines[y][x]))
            heat_loss_map[y].append(sys.maxsize)
    heat_loss_map[height-1][width-1] = 0
    ret = 0
    queue = list()

    def graph_fn2(state):
        x, y, dx, dy, same_directions = state
        if same_directions < 10:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < width and 0 <= new_y < height:
                new_state = (new_x, new_y, dx, dy, same_directions+1)
                yield new_state, city_map[new_y][new_x]
        if same_directions >= 4:
            new_x, new_y = x+dy, y-dx
            if 0 <= new_x < width and 0 <= new_y < height:
                new_state = (new_x, new_y, dy, -dx, 1)
                yield new_state, city_map[new_y][new_x]
            new_x, new_y = x-dy, y+dx
            if 0 <= new_x < width and 0 <= new_y < height:
                new_state = (new_x, new_y, -dy, dx, 1)
                yield new_state, city_map[new_y][new_x]
    def graph_fn(state):
        x, y, dx, dy, same_directions = state
        for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            new_dx = new_x - x
            new_dy = new_y - y
            if new_dx == dx and new_dy == dy:
                if same_directions == 10:
                    continue
                new_same_directions = same_directions + 1
            elif new_dx == -dx and new_dx != 0:
                continue
            elif new_dy == -dy and new_dy != 0:
                continue
            else:
                if same_directions < 4:
                    continue
                new_same_directions = 1

            if 0 <= new_x < width and 0 <= new_y < height:
                new_state = (new_x, new_y, new_dx, new_dy, new_same_directions)
                yield new_state, city_map[new_y][new_x]

    queue = list()

    graph = utils.make_graph(graph_fn)
    ## answer has bug lol. holy shit. so here I used a boundary value to get a "RIGHT" one
    heapq.heappush(queue, (0, (0, 0, -1, 0, 4)))

    # graph = utils.make_graph(graph_fn2)
    #heapq.heappush(queue, (0, (0, 0, 1, 0, 0)))
    #heapq.heappush(queue, (0, (0, 0, 0, 1, 0)))
    heapq.heapify(queue)
    while queue:
        curr_loss, current_node = heapq.heappop(queue)
        x, y = current_node[0], current_node[1]
        heat_loss_map[y][x] = curr_loss
        if current_node in seen:
            continue
        seen.add(current_node)
        if x == width - 1 and y == height - 1:
            ret = curr_loss
            break
        for neighbour_node, neighbour_loss in graph[current_node]:
            if neighbour_node in seen:
                continue
            heapq.heappush(queue, (curr_loss+neighbour_loss, neighbour_node))
    print(ret)


if __name__ == "__main__":
    #solution_1()
    solution_2()