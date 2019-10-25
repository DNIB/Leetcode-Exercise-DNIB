class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key = []
        self.value = []
        self.size = 0
        self.max_size = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            temp = self.key.index(key)
            k, v = self.key[temp], self.value[temp]
            del self.key[temp]
            del self.value[temp]
            self.key.insert(0, k)
            self.value.insert(0, v)
            return v
        except:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        try:
            i = self.key.index(key)
            del self.key[i]
            del self.value[i]
            
        except:
            if self.size < self.max_size:
                self.size += 1
            else:
                self.key.pop()
                self.value.pop()
                
        self.key.insert(0, key)
        self.value.insert(0, value)
    
    def show(self):
        print(self.key)
        print(self.value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)