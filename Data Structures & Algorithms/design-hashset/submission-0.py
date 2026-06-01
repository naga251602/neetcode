class MyHashSet:

    def __init__(self):
        self.lim = 10_000
        self.st = [-1] * self.lim

    def add(self, key: int) -> None:
        pos = key%self.lim
        
        for i in range(pos, self.lim):
            if self.st[i] == key: return
            elif self.st[i] == -1: break
        
        self.st[i] = key

    def remove(self, key: int) -> None:
        pos = key%self.lim
        
        for i in range(pos, self.lim):
            if self.st[i] == key: 
               self.st[i] = -1
               break
     
    def contains(self, key: int) -> bool:
        pos = key%self.lim
        for i in range(pos, self.lim):
            if self.st[i] == key: return True
            elif self.st[i] == -1: break
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)