from graph import *


data_path = "input/"
file_name = "network.01.in"

g = Graph.graph_from_file(data_path + file_name)
print(g)

print(kruskal(g))