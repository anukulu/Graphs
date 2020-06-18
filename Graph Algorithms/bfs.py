from graphMaker import MakeGraph
from queue import Queue as Q

n = int(input("Enter the number of nodes in the graph : "))
g = MakeGraph.UnweightedUndirectedGraphCreator(n)

visited = [False for _ in range(n)]
values = []

def Solve(temp):
    at = temp - 1
    prev = [None for _ in range(n)]
    q = Q()
    q.Enqueue(g[at])
    visited[at] = True

    while(not q.IsEmpty()):
        node = q.Dequeue()
        values.append(node.iD)
        neighbors = node.neighbors

        if(neighbors == None):
            continue
        for x in neighbors:
            if (not visited[x.iD - 1]):
                q.Enqueue(x)
                visited[x.iD - 1] = True
                prev[x.iD - 1] = node.iD
    return prev

def ConstructedPath(s, e, prev):
    at = e - 1
    path = []
    path.append(e)
    while(prev[at] != None):
        path.append(prev[at])
        at = prev[at] - 1 
    path.reverse()
    if path[0] == s:
        return path
    return []


def BFS(s, e):
   prev = Solve(s)

   return ConstructedPath(s, e, prev)

a = BFS(1,3)
print(a)


