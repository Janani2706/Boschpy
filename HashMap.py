class SimpleHashMap:
    def __init__(self, capacity=2):
        self.capacity = capacity 
        self.buckets = [[] for _ in range(capacity)]
 
    def _hash(self, key):
        return hash(key) % self.capacity
 
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value))
 
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
 
    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[idx]
                return True
        return False
 
    def __str__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return '{' + ', '.join(f"{k}: {v}" for k, v in items) + '}'
hashmap = SimpleHashMap()
hashmap.put("a", 100)
hashmap.put("b",80)
print("Initial hashmap:", hashmap)
hashmap.put("a", 200)  
print("After updating a:", hashmap) 
print("Get a:", hashmap.get("a"))
print("Get c:", hashmap.get("o"))
hashmap.remove("b")
print("After removing b:", hashmap)