from graph import Graph

def help1(list_nodes):
    dict_nodes = {}
    for node in list_nodes:
        dict_nodes[node.value] = node
    return dict_nodes

def help2(list_nodes):
    neighbors = {}
    for node in list_nodes:
        neighbors[node[0].value] = node
    return neighbors

def get_edge(graph, arr):

    dict_nodes = help1(graph.get_nodes())
    trip_price = 0

    for i in range (0, len(arr)-1):

        if arr[i] not in dict_nodes:
            return False, '$0'

        if arr[i] in dict_nodes:
            neighbors_dict = help2(graph.get_neighbors(dict_nodes[arr[i]]))

            if arr[i+1] in neighbors_dict:
                trip_price += neighbors_dict[arr[i+1]][1]

            else:
                return False, '$0'


    return True, f'${trip_price}'