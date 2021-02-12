import numpy as np
import heapq
from graph import Node, Graph
from utils import compute_pythagorean_distance


def search(start, use_heuristics=False):
    visited = set()                  
    q = []    #priority queue
                                    
    q.append((0, start.vertex_id, start, 0))  #store cost including h(x), start vertex_id, start vertex, and cost without h(x)
    heapq.heapify(q)
    cnt = 0
    while(len(q)>0):
        total_cost, _, current_node, cost = q[0]
        del q[0]
        heapq.heapify(q)

        cnt+=1
        
        if current_node.is_goal:
            print('Reached goal node %s. Visited %s nodes. Cost: %s'%(current_node.vertex_id, cnt, cost))
            return

        visited.add(current_node)

        for edge in current_node.out_edges:
            child = edge.to()

            new_cost = total_cost + edge.weight
            if use_heuristics:
                h = compute_pythagorean_distance(current_node.square_id, child.square_id)
                new_cost += h

            if child not in visited and not any(item[2]==child for item in q):
                q.append((new_cost, child.vertex_id, child, cost+edge.weight))
                heapq.heapify(q)
            elif any(item[2]==child and item[0]>new_cost for item in q):
                del q[np.argmax([item[2]==child for item in q])]
                q.append((new_cost, child.vertex_id, child, cost+edge.weight))
                heapq.heapify(q)
            
    return 'No path found'


def run():
    graph = Graph()
    graph.read_graph('p1_graph.txt')
    print('UCS')
    search(graph.source)
    print('A*')
    search(graph.source, True)   


if __name__=='__main__':
    run()