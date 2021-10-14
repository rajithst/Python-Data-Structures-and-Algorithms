from collections import deque

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
source = 0
target = len(graph) - 1


def all_path_src_to_target_bfs():
    que = deque()
    que.append([source])
    result = []

    while que:
        cr = que.popleft()
        if cr[-1] == target:
            result.append(cr)
        else:
            for n in graph[cr[-1]]:
                que.append(cr + [n])

    print(result)
all_path_src_to_target_bfs()
