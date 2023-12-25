from collections import defaultdict
import utils
import igraph

def solution_1(data_lines: list[str]):
    graph =  defaultdict(set)
    for line in data_lines:
        left, rights = line.split(": ")
        rights = rights.split(" ")
        graph[left] = set(rights)
        # for r in rights:
        #     graph[r].add(left)
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
    for node in graph:
        if not visited[node]:
            dfs(node, None, visited, disc, low, bridges)
    print("Bridges:", bridges)
    cut = igraph.Graph.ListDict(graph).mincut()
    print(len(cut[0])*len(cut[1]))

def solution_2(data_lines: list[str]):
    pass

if __name__ == "__main__":
    data_lines = utils.get_file_content("day25.dat")
    data_lines = [l.strip() for l in data_lines]
    solution_1(data_lines)
    solution_2(data_lines)