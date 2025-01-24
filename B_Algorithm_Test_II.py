import collections

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node, new_node):
        new_node.prev = node
        if node.next:
            new_node.next = node.next
            node.next.prev = new_node
        node.next = new_node
        if node == self.tail:
            self.tail = new_node

    def remove(self, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def pushback(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

def process_queries(q, queries):
    linked_list = LinkedList()
    nodes = collections.defaultdict(collections.deque)

    for query in queries:
        if query[0] == "insert":
            new_node = ListNode(query[1])

            if query[2] in nodes:
                linked_list.insert(nodes[query[2]][0], new_node)
            else:
                linked_list.pushback(new_node)

            nodes[query[1]].append(new_node)

        elif query[0] == "remove":
            if query[1] in nodes:
                node = nodes[query[1]].popleft()
                linked_list.remove(node)
                if not nodes[query[1]]:
                    nodes.pop(query[1])

    return linked_list

def print_linked_list(linked_list):
    current = linked_list.head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def main():
    q = int(input().strip())
    queries = [input().strip().split() for _ in range(q)]
    linked_list = process_queries(q, queries)
    print_linked_list(linked_list)

if __name__ == "__main__":
    main()
