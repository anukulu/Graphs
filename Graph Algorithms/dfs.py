from graphMaker import MakeGraph

n = int(input("Enter the number of nodes in the graph : "))
g = MakeGraph.UnweightedUndirectedGraphCreator(n)

n = len(g)

visited = [False for _ in range(n)]
values = []

def DFS(temp):
    at = temp-1
    if (visited[at] == True):
        return
    visited[at] = True
    values.append(g[at].iD)
    if(g[at].neighbors == None):
        return
    for neighbor in g[at].neighbors:
        DFS(neighbor.iD)

def StronglyConnectedComponents():
    count = 0
    for x in range(n):
        if(not visited[x]):
            count += 1
            DFS(g[x].iD)
    return count

ct = StronglyConnectedComponents()
print([values, ct])