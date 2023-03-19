from example_graphs import *

def graph_traversal(graph, start_node, mode='breadth'):
    '''
    Returns the traversal of the input graph
    graph     : Input graph in adjacency list representation
    start_node: Start node/vertex for traversal
    mode      : Traversal mode 'depth' or 'breadth', defaults to 'depth'
    '''
    stack = [start_node]
    mode_idx = {'depth': -1, 'breadth': 0}[mode]
    r = []
    while(len(stack)>0):
        node = stack.pop(mode_idx)
        r.append(node)
        for neighbour in graph[node]:
            if (not neighbour in r) and (not neighbour in stack):
                stack.append(neighbour)
    return r


def find_path_s(graph, start_node, end_node, return_type='all'):
    '''
    Returns the path(s) from the start node to the end node
    graph      : Input graph in adjacency list representation
    start_node : Start node of path
	end_node   : End node of path
	return_type: Defaults to 'all' to return all paths, 'shortest' returns only the shortest path
    '''
    if start_node == end_node:
        return [[start_node]]
    return_shortest = {'shortest': True, 'all': False}[return_type]
    path_found = False
    no_path = False
    path_list = [[start_node]]
    temp_path_list = []
    good_paths = []
    while (not (path_found and return_shortest)) and (not no_path):
        for path in path_list:
            paths = []
            for neighbour in graph[path[-1]]:
                if not neighbour in path:
                    paths.append(path + [neighbour])
                    if neighbour == end_node:
                        path_found = True
                        good_paths.append(path + [neighbour])
            temp_path_list += paths
        if temp_path_list == []:
            no_path = True
        else:
            path_list = temp_path_list
            temp_path_list = []
    return good_paths


def connected_components(graph, mode='breadth'):
    '''
    Returns all traversals of components of an undirected graph
    graph: Input undirected graph ub adjacency list representation
    mode : Traversal mode 'depth' or 'breadth', defaults to 'depth' 
    '''
    visited_nodes = []
    components = []
    for node in graph:
        if not node in visited_nodes:
            component_traversal = graph_traversal(graph, node, mode)
            components.append(component_traversal)
            visited_nodes += component_traversal
    return components


def largest_connected_component_s(graph, mode='breadth'):
    '''
    Returns the largest component(s) of an undirected graph
    graph: Input undirected graph ub adjacency list representation
    mode : Traversal mode 'depth' or 'breadth', defaults to 'depth' 
    '''
    component_list = connected_components(graph, mode)
    largest_component_size = max([len(component) for component in component_list])
    largest_component_s = [component for component in component_list if largest_component_size == len(component)]
    if 1 == len(largest_component_s):
        largest_component_s = largest_component_s[0]
    return largest_component_s


def pathExists(graph, start_node, end_node, mode='breadth'):
    '''
    Returns True/False for if start_node to end_node path exists in the intput graph
    graph     : Input graph in adjacency list representation
    start_node: Start node/vertex
    end_node  : End node/vertex
    mode      : Traversal mode 'depth' or 'breadth', defaults to 'depth'
    '''
    if start_node == end_node:
        return True
    stack = [start_node]
    mode_idx = {'depth': -1, 'breadth': 0}[mode]
    r = []
    while(len(stack)>0):
        node = stack.pop(mode_idx)
        r.append(node)
        if end_node in graph[node]:
            return True
        for neighbour in graph[node]:
            if (not neighbour in r) and (not neighbour in stack):
                stack.append(neighbour)
    return False


def edges_to_adj_list(edge_list):
    '''
    Returns the adjacency representation of an undirected graph from an input of edge list
    edge_list: list of nodes connected by edges
    '''
    adj_list = {}
    for edge in edge_list:
        if not edge[0] in adj_list:
            adj_list[edge[0]] = []
        if not edge[1] in adj_list:
            adj_list[edge[1]] = []
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    return adj_list






def adj_to_mat_rep(adj_rep):
    '''
    Returns the matrix representation of an adjacency list representation
    adj_rep: adjacency representation with all nodes as numbers
    '''
    size = len(adj_rep)
    mat_rep = [[0 for n in range(size)] for n in range(size)]
    for node in adj_rep:
        for vertex in adj_rep[node]:
            mat_rep[node][vertex] = 1
    return mat_rep


def print_mat_rep(mat_rep):
    '''
    Prints matrix representation
    mat_rep: matric representation to print
    '''
    blank_print = (2 * len(mat_rep) + 1) * ' '
    print('/' + blank_print + '\\')
    for row in mat_rep:
        print('| ', end='')
        for element in row:
            print(element, end=' ')
        print('|')
    print('\\' + blank_print + '/')
