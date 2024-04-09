#  write a program to implement Uniform cost search for following graph.Consider initial node is Arad and final state is Bucharest.Display Final path cost.
# arad->timisora->Lugoj->Mehadia->Drobeta->Craivo->


# Graph representation 
from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current_cost, current_node = frontier.get()

        if current_node == goal:
            break

        for next_node, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                frontier.put((priority, next_node))
                came_from[next_node] = current_node

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
   
    return path, cost_so_far[goal]
                                            
graph = {
    'arad': {'sibiu': 140, 'timisoara': 128},
    'sibiu': {'arad': 140, 'fagaras': 99, 'rimnicu': 80},
    'timisoara': {'arad': 118, 'lugoj': 111},
    'lugoj': {'timisoara': 111, 'mehadia': 70},
    'mehadia': {'lugoj': 70, 'drobeta': 75},
    'drobeta': {'mehadia': 75, 'craiova': 120},
    'craiova': {'drobeta': 130, 'rimnicu': 146, 'pitesti': 138},
    'rimnicu': {'sibiu': 80, 'craiova': 146, 'pitesti': 97},
    'fagaras': {'sibiu': 99, 'bucharest': 211},
    'pitesti': {'craiova': 138, 'rimnicu': 97, 'bucharest': 101},
    'bucharest': {'fagaras': 211, 'pitesti': 101}
}

start_node = 'arad'
goal_node = 'bucharest'

path, cost = uniform_cost_search(graph, start_node, goal_node)
print("Path:", path)
print("Cost:", cost)