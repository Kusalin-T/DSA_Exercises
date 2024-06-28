
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

def bfs_q(s, e, routes, visited=[]):
    queue = [s]
    while queue:
        queue=list(set(queue)) #modified to bugfix
        current = queue.pop(0)
        if current==e:
            print('Path: ' + '-->'.join(visited) + '-->' + e)
            return
        visited.append(current)
        for node in (routes[current]-set(visited)):
            queue.append(node)
    print('No Path Found')

# I believe my recursive function was actually better
# it seems that this approach created the possibility of duplicate visits
# I modified line 27 to fix this
bfs_q('A', 'F', data)            