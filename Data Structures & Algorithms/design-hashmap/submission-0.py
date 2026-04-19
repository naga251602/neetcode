class MyHashMap:

    def __init__(self):
        self.lim = 10_000
        self.st = [(-1, -1)] * self.lim

    def put(self, key: int, value: int) -> None:
        pos = key%self.lim
        
        for i in range(pos, self.lim):
            if self.st[i][0] == key: 
                self.st[i] = (key, value)
            elif self.st[i] == (-1, -1): break
        
        self.st[i] = (key,value)

    def get(self, key: int) -> int:
        pos = key%self.lim
        
        for i in range(pos, self.lim):
            if self.st[i][0] == key: return self.st[i][1]
            elif self.st[i] == (-1, -1): return -1

    def remove(self, key: int) -> None:
        pos = key%self.lim
        
        for i in range(pos, self.lim):
            if self.st[i][0] == key: 
                self.st[i] = (-1, -1)
            elif self.st[i] == (-1, -1): break
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)