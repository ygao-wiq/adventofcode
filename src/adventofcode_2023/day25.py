from collections import defaultdict
import utils
import igraph

def solution_1(data_lines: list[str]):
    graph =  defaultdict(list)
    for line in data_lines:
        left, rights = line.split(": ")
        rights = rights.split(" ")
        graph[left] = rights
    cut = igraph.Graph.ListDict(graph).mincut()
    print(len(cut[0])*len(cut[1]))

def solution_2(data_lines: list[str]):
    graph =  defaultdict(list)
    for line in data_lines:
        left, rights = line.split(": ")
        rights = rights.split(" ")
        graph[left].extend(rights)
        for r in rights:
            graph[r].append(left)
    visited = {node: False for node in graph}
    disc = {node: float('inf') for node in graph}
    low = {node: float('inf') for node in graph}
    bridges = []
    time = 0
    def dfs(node, parent, visited, disc, low, bridges):
        nonlocal time
        visited[node] = True
        disc[node] = time
        low[node] = time
        time += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, node, visited, disc, low, bridges)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append((node, neighbor))
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])

    dfs([k for k in graph.keys()][0], None, visited, disc, low, bridges)
    print("Bridges:", bridges)
    # bridges = [("hfx", "pzl"), ("bvb", "cmg"), ("nvd", "jqt")]
    for v1, v2 in bridges:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
    sub1 = set()
    todo = [[k for k in graph.keys()][0]]
    while todo:
        v = todo.pop(0)
        if v in sub1:
            continue
        sub1.add(v)
        todo.extend(graph[v])
    print(sub1)
    sub2 = set([k for k in graph.keys() if k not in sub1])
    print(sub2)
    print(len(sub1)*len(sub2))
        

if __name__ == "__main__":
    data_lines = utils.get_file_content("day25.dat")
    data_lines = [l.strip() for l in data_lines]
    solution_1(data_lines)
    # solution_2(data_lines)