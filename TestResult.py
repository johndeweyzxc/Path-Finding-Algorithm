from Graph import Graph

graph = Graph()
# graph.add_edge('Vertex', 'Vertex', integer weights or length between the two vertex)
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'D', 3)
graph.add_edge('B', 'E', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('C', 'F', 1)
graph.add_edge('D', 'F', 3)
graph.add_edge('E', 'F', 13)
graph.add_edge('F', 'G', 8)
graph.add_edge('F', 'H', 2)
graph.add_edge('G', 'H', 1)
graph.add_edge('H', 'E', 1)
graph.add_edge('H', 'X', 14)

# graph.path_finding('Source vertex', 'Destination vertex')
print(graph.path_finding('A', 'X'))
