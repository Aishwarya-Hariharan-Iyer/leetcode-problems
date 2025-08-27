class MyHashMap(object):

    def __init__(self):
        self.hashmap = []
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hasKey = len(filter(lambda x: x[0] == key, self.hashmap)) != 0
        if not hasKey:
            self.hashmap += [[key, value]]
        else:
           self.hashmap = map(lambda x: [x[0], value] if x[0] == key else x, self.hashmap)  
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        key_val = filter(lambda x: x[0] == key, self.hashmap)
        if len(key_val) == 0:
            return -1
        else:
            return key_val[0][1]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        l = len(self.hashmap)
        for i in range(l):
            key_i = self.hashmap[i][0]
            if key_i == key:
                self.hashmap = (self.hashmap[:i] if i != 0 else []) + (self.hashmap[i+1:] if i+1 < l else [])
                break
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
