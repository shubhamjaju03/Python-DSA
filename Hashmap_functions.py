class Hashmaps:
    def __init__(self,capacity):
        self.capacity=capacity
        self.slots=[None]*self.capacity
        self.value=[None]*self.capacity
        self.size=0

    def hash_function(self,key):
        return abs(hash(key))% self.capacity
    
    def rehash(self,old_hash):
        return (old_hash+1)% self.capacity
    
    def insert(self,key,value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value]=key
            self.value[hash_value]=value
            self.size += 1
        else:
            if self.slots[hash_value]==key:
                self.value[hash_value]=value
            else:
                new_hash = self.rehash(hash_value)
                # Loop until empty slot or same key found
                while self.slots[new_hash] is not None and self.slots[new_hash]!=key:
                    new_hash = self.rehash(new_hash)
                    if new_hash == hash_value:  # avoids infinite loop in full table
                        break
                if self.slots[new_hash]==None:
                    self.slots[new_hash]=key
                    self.value[new_hash]=value
                    self.size += 1
                elif self.slots[new_hash]==key:
                    self.value[new_hash]=value

    def get(self, key):
        hash_value = self.hash_function(key)
        index = hash_value
        start_index = index
        
        while self.slots[index] is not None:
            if self.slots[index] == key:
                return self.value[index]
            index = self.rehash(index)
            if index == start_index:
                break
        return None

    def delete(self,key):
        hash_value = self.hash_function(key)
        index = hash_value
        start_index = index
        while self.slots[index] is not None:
            if self.slots[index] == key:
                self.slots[index] = None
                self.value[index] = None
                self.size -= 1
                return
            index = self.rehash(index)
            if index == start_index:
                break
        return False
