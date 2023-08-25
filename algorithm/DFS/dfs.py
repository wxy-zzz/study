tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: [],
}

def dfs(tree, start_node):
    visit = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(tree[node])

    return visit

print(dfs(tree, 1))
