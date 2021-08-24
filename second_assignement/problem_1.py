class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = Node(value)
            return
        
        node = self.tail
        node.next = Node(value)
        node.next.previous = node
        self.tail = node.next
    
    def to_list(self):
        _list = []
        head = self.head
        while head is not None:
            _list.append(head.value)
            head = head.next
        return _list
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.usage_rank = DoublyLinkedList()
        self.num_elements = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            
            return self.cache[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.num_elements == 0:
            self.cache[key] = value
            self.usage_rank.append(key)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(
    our_cache.get(3)
)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
