from typing import OrderedDict

class LRUCacheUsingOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                # remove LRU and add new key value
                self.cache.popitem(False)

            self.cache[key] = value
            self.cache.move_to_end(key)

        print(f"current cache: {self.cache}")


class Node:
    def __init__(self, key: int, value: int):
        self.next = None
        self.prev = None
        self.val = value
        self.key = key

class LRUCacheUsingDoublyLinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-2, -2)

        self.left.next = self.right
        self.right.prev = self.left

    def insertMostRecentlyUsedNode(self, node: Node):
        former_most_recent = self.right.prev

        self.right.prev = node
        node.next = self.right
        node.prev = former_most_recent
        former_most_recent.next = node

    def removeNode(self, node: Node):
        left_of_node = node.prev
        right_of_node = node.next
        left_of_node.next = right_of_node
        right_of_node.prev = left_of_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.insertMostRecentlyUsedNode(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.removeNode(node)
            self.insertMostRecentlyUsedNode(node)
        else:
            if len(self.cache) == self.capacity:
                least_recently_used_node = self.left.next
                self.removeNode(least_recently_used_node)
                self.cache.pop(least_recently_used_node.key)

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insertMostRecentlyUsedNode(new_node)


