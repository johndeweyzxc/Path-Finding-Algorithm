class Node:
    def __init__(self, data, weight, nxt=None):
        self.data = data
        self.weight = weight
        self.next = nxt


# This priority queue is just a linked list but
# the order in which the node sits depends on
# the weight of the node.

# The queue stores a list of linked list which is
# a path to determine who is the shortest
# path.
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    # Push the node into the queue
    def enqueue(self, item, item_weight):
        node_queue = Node(item, item_weight)

        # Queue is empty therefore set the first item as head
        if self.head is None:
            self.head = node_queue
            self.size += 1
            return

        # If head is not none
        current = self.head
        previous = None

        while current:
            # Push the new node on the end of the list until the current
            # node is less than or equals to the weight of the new
            # node.

            # [1] -> [3] -> [4]
            if current.weight > item_weight:
                node_queue.next = current
                if previous:
                    previous.next = node_queue
                    break
                else:
                    self.head = node_queue
                    break
            elif current.weight <= item_weight:
                if current.next is None:
                    current.next = node_queue
                    break

            # Previous will become the current node and the
            # current will be the next node
            previous = current
            current = current.next

        self.size += 1

    # Remove the first item in the list
    def dequeue(self):
        if self.head is None:
            raise IndexError('pop from empty queue')

        head_data = self.head
        # Replace the head with the next node of current head
        self.head = self.head.next
        return head_data.data, head_data.weight


