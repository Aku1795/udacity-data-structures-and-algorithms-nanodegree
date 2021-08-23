class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.operations = dict()
        self.num_elements = 0
        self.min_key = None
        self.min_operations = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.operations[key] += 1
            self.update_min_key(key)
            return  self.cache[key]
        return -1
    
    def update_min_key(self, key):
        if self.operations[key] <= self.min_operations:
            self.min_operations = self.operations[key]
            self.min_key = key

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.num_elements == 0:
            self.min_key = key
            self.cache[key] = value
            self.operations[key] = 1
            self.min_operations = self.operations[key]
            self.num_elements += 1
        elif self.num_elements < self.capacity:
            self.cache[key] = value
            self.operations[key] = 1
            self.num_elements += 1
            self.update_min_key(key)
        else:
            del self.operations[self.min_key]
            del self.cache[self.min_key]
            self.cache[key] = value
            self.operations[key] = 1
            self.min_key = key
            self.min_operations = 1      
        



our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
