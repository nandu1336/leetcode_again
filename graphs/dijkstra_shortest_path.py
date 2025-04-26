import math 


def find_shortest_path(graph, to, _from='a'):
    network = {}
    cost = {}

    for node in graph:
        source, destination, weight = node
        if source in network:
            network[source].append((destination, weight))
        else:
            network[source] = [(destination, weight)]
            cost[source] = math.inf
    
    cost[_from] = 0
    visited = set()
    queue = set()

    def traverse(network, node):
        nonlocal queue

        if node not in visited: 
            visited.add(node)
            
            for neighbour, weight in network[node]:
                if neighbour not in visited: 
                    queue.add(neighbour)
                    cost_from_node = cost[node] + weight
                    
                    if cost[neighbour] > cost_from_node:
                        cost[neighbour] = cost_from_node

            while queue:
                traverse(network, queue.pop())
        
    traverse(network, 'a'), cost
    return cost[to]
            

if __name__ == "__main__":
        
    graph = [('a', 'c', 3), ('c', 'a', 3), 
            ('a', 'f', 2), ('f', 'a', 2),
            ('c', 'f', 2), ('f', 'c', 2), 
            ('c', 'd', 4), ('d', 'c', 4), 
            ('c', 'e', 1), ('e', 'c', 1),
            ('f', 'e', 3), ('e', 'f', 3),
            ('f', 'b', 6), ('b', 'f', 6), 
            ('f', 'g', 5), ('g', 'f', 5), 
            ('g', 'b', 2), ('b', 'g', 2),
            ('d', 'b', 1), ('b', 'd', 1), 
            ('e', 'b', 2), ('b', 'e', 2)]
    print(find_shortest_path(graph, 'b'))