class MyHashMap:

    def __init__(self):
        self.pairs = []
        

    def put(self, key: int, value: int) -> None: 
        for i in range(len(self.pairs)): 
            if self.pairs[i][0] == key: 
                self.pairs[i][1] = value
                return 
        
        self.pairs.append([key,value])
        

    def get(self, key: int) -> int: 
        for i in range(len(self.pairs)): 
            if self.pairs[i][0] == key: 
                return self.pairs[i][1]
        return - 1 
            
        

    def remove(self, key: int) -> None: 
        for i in range(len(self.pairs)): 
            if self.pairs[i][0] == key: 
                self.pairs.pop(i)
                return 
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)