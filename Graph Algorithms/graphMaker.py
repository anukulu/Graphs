
# only works for unweighted graphs for now

class Node:
    def __init__(self, iD):
        self.iD = iD

    def Info(self, neighbors=None, extraInfo=None):
        self.neighbors = neighbors
        self.extraInfo = extraInfo

class MakeGraph:

    @staticmethod
    def UnweightedUndirectedGraphCreator(n):
        
        graph = [Node(i+1) for i in range(n)]
        # print("Enter the graph_iD, spacebar,  graph neighbors' index with no spaces, spacebar, any info related to the graph")
        valid = True
        for x in graph:
            nodeInfo = input().split(" ")
            neighbors = []
            if(len(nodeInfo) < 2):
                x.Info()
                continue
            for y in nodeInfo[1]:
                if(int(y) > len(graph)):
                    valid = False
                    break
                else:
                    neighbors.append(graph[int(y)-1])
            if(not valid):
                print("ids of nodes must be less than or equal to the size of graph and start the first node from 1")
                return None
            if(len(nodeInfo) > 2):
                x.Info(neighbors , nodeInfo[2])
            else:
                x.Info(neighbors)
        valid = MakeGraph.GraphValidity(graph)
        if(not valid):
            return None
        return graph
    
    @staticmethod
    def GraphValidity(graph):
        valid = True
        for node in graph:
            if(node.neighbors == None):
                continue
            for neighbor in node.neighbors:
                if (node in neighbor.neighbors):
                    continue
                else:
                    valid = False
                    break
            if(not valid):
                break
        return valid



