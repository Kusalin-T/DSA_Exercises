
data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
}
#Intended Implementation seems to be with a Queue, but this works too
def bfs(s, e, routes, path=[]):
    for r in routes[s]:
        if r in path:
            continue
        if s == e:
            return path + [s]
        if r == e:
            return path + [s] + [e]
        else:
            return bfs(r, e, routes, path+[s])
        
print(bfs('A', 'F', data))