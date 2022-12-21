from PriorityQueue import PriorityQueue
from LinkedLists import LinkedLists


# This prints the result of the shortest path.
def format_result(found_path, total_weight):
    paths = found_path.read_list_data()
    res_keys = ''
    res_keys += '['
    i = 0
    for p in paths:
        if i == len(paths) - 1:
            res_keys += p
        else:
            res_keys += p + ' -> '
        i += 1
    res_keys += ']'
    return f'\nShortest path: {res_keys}\nTotal weight: {total_weight}'


class Vertex:
    def __init__(self, prev_key, key, weight):
        self.prev_key = prev_key
        self.key = key
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertex_col = {}

    def add_vertex(self, key):
        self.vertex_col[key] = []

    def get_vertex(self, key):
        if key in self.vertex_col:
            return self.vertex_col[key]
        return None

    def add_edge(self, node1, node2, weight):
        if node1 not in self.vertex_col:
            self.add_vertex(node1)
        if node2 not in self.vertex_col:
            self.add_vertex(node2)

        # Connects node1 to node2
        self.vertex_col[node1].append(
            Vertex(node1, node2, weight))

    def path_finding(self, start, end):
        paths = None
        new_weight = None

        queue = PriorityQueue()
        while start != end:
            # Get all the connections
            current_v = self.get_vertex(start)

            # Calculate all the weight of each connection of the
            # current vertex.
            for v in current_v:
                linkist = LinkedLists()
                if paths is not None:
                    # Combine the path with the previous path that we have.
                    linkist.join_list(paths)

                if linkist.size == 0:
                    linkist.append(start, start, 0)

                linkist.append(v.prev_key, v.key, v.weight)
                # Calculate the weight
                link_weight = linkist.calc_weight()
                # Push into priority queue, the smallest weight is the first
                # node in the queue.
                queue.enqueue(linkist, link_weight)

            # Dequeuing in priority queue returns the shortest path from the start vertex
            # up to the current vertex.
            new_priority, new_weight = queue.dequeue()
            # Set the best shortest path for now
            paths = new_priority
            # Now the starting vertex is now the last vertex of the current best shortest path
            # that we have. As long as the start vertex is not the end vertex, we continue
            # exploring all the connected paths of last vertex and calculate their weights.
            start = new_priority.tail.key

        return format_result(paths, new_weight)
