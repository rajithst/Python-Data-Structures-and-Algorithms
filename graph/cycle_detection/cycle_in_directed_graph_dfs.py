vertices = [0, 1, 2, 3, ]
edges = [(0, 1), (1, 2), (1, 3), (3, 2)]
# visited dictionary to keep track of visited nodes during all dfs calls
visited = {v: False for v in vertices}

# call stack dictionary to keep track of dfs calls within a current path
callstack = {v: False for v in vertices}
adj_list = {}
for x, y in edges:
    if x not in adj_list:
        adj_list[x] = []
    if y not in adj_list:
        adj_list[y] = []
    adj_list[x].append(y)


def dfs(node, callstack):
    #mark global visited dic as true,mark callstack node as true
    visited[node] = True
    callstack[node] = True

    #recursively call dfs for all adj nodes
    for nei in adj_list[node]:
        #if current node in the callstack,which means a cycle,return true
        if callstack[nei]:
            return True
        # otherwise if node is not visited,perform dfs on neibhr
        elif not visited[nei]:
            cycle_found = dfs(nei, callstack)
            if cycle_found:
                return True
    #make node as false when backtracking
    callstack[node] = False
    #return false when backtracking
    return False


def dfs_wrapper():
    for v in vertices:
        if not visited[v]:
            if dfs(v, callstack):
                return "Cycle Found"
    return "Cycle Not Found"


print(dfs_wrapper())
