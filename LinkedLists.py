class Node:
    def __init__(self, prev_key, key, weight):
        self.prev_key = prev_key
        self.key = key
        self.weight = weight
        self.next = None


# This is the linked lists to create a list of path, each node has weights.
# For example path [A] to [B], going to [B] from [A] has a weight of 10.
# The next of node [A] is [B]. The previous of [B] is node [A].
class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def read_list(self):
        node_data = []
        node = self.head

        # Traverse through the linked list by replacing
        # the current node with the next node until
        # the next node is null.
        while node is not None:
            node_data.append(node)
            node = node.next

        return node_data

    def read_list_data(self):
        nodes = self.read_list()
        node_data = {}
        for n in nodes:
            node_data[n.key] = n.weight
        return node_data

    def calc_weight(self):
        nodes = self.read_list()
        weight = 0
        for n in nodes:
            weight += n.weight
        return weight

    # Append the node in list
    def append(self, prev_key, key, weight):
        node = Node(prev_key, key, weight)

        # The tail is the last node in the list, appending a node is
        # just replacing the next of the tail node with the new node
        # then replacing tail with the new inserted node
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    # Combine two linked lists together, by reading its value
    # and making new nodes to attach to the current lists.
    def join_list(self, link):

        # The link is just another linked lists that we will be
        # joining with this current linked lists
        link_list = link.read_list()
        for i in link_list:
            self.append(i.prev_key, i.key, i.weight)
