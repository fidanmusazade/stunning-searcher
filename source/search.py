import numpy as np
import heapq
from graph import Node, Graph
from utils import generate_coordinates



def search(start, use_heuristics=False, coordinates=None):
    visited = set()                  
    q = []    #priority queue
                                    
    q.append((0, start.vertex_id, start, 0))
    heapq.heapify(q)
    while(len(q)>0):
        cost, _, current_node, usual_cost = q[0]
        del q[0]
        heapq.heapify(q)
        
        if current_node.is_goal:
            print('Reached goal node %s. Visited %s nodes. %s'%(current_node.vertex_id, len(visited), usual_cost))
            return

        visited.add(current_node)
        # print('Expands node \'%s\' with cumulative cost %s ...' % (current_node.vertex_id, cost))

        for edge in current_node.out_edges:
            child = edge.to()

            cumulative_cost = cost + edge.weight
            if use_heuristics:
                # horiz_distance = (np.abs(current_node.square_id%10-child.square_id%10)+1)*1000
                # vert_distance = (np.abs(current_node.square_id//10-child.square_id//10)+1)*1000
                # h = c_h(current_node.square_id, child.square_id)
                # h = np.sqrt(horiz_distance*horiz_distance+vert_distance*vert_distance)
                current_square = coordinates[current_node.square_id]
                child_square = coordinates[child.square_id]
                h = np.linalg.norm(current_square-child_square)
                cumulative_cost += h

            if child not in visited and not any(item[2]==child for item in q):
                q.append((cumulative_cost, child.vertex_id, child, usual_cost+edge.weight))
                heapq.heapify(q)
            elif any(item[2]==child and item[0]>cumulative_cost for item in q):
                del q[np.argmax([item[2]==child for item in q])]
                q.append((cumulative_cost, child.vertex_id, child, usual_cost+edge.weight))
                heapq.heapify(q)
            
    return 'No path found'

def run():
    # graph, source = read_graph('p1_graph.txt')
    graph = Graph()
    graph.read_graph('p1_graph.txt')
    coordinates = generate_coordinates()
    print('UCS')
    search(graph.source)
    print('A*')
    search(graph.source, True, coordinates)   

# def test(source, destination):
#     graph, source = read_graph('p1_graph.txt')
#     coordinates = generate_coordinates()
#     graph.nodes[99].is_goal = False
#     graph.nodes[destination].is_goal = True
#     print('UCS')
#     search(graph.nodes[source])
#     print('A*')
#     search(graph.nodes[source], True, coordinates) 


if __name__=='__main__':
    run()
    # source, destination = map(int, input().split())
    # test(source, destination)