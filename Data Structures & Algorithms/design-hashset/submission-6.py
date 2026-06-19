class MyHashSet:
    def __init__(self):
        self.st = [-1] * 10000


    def add(self, key: int) -> None:
        if self.contains(key): return
        
        pos = key%10000
        if self.st[pos] == -1: self.st[pos] = key
        else:
            for i in range(pos, 10000):
                if self.st[i] == -1: 
                    self.st[i] = key
                    break
    
    def remove(self, key: int) -> None:
        pos = key%10000
        if self.st[pos] == key: 
            self.st[pos] = -1
        else:
            for i in range(pos, 10000):
                if self.st[i] == key: 
                    self.st[i] = -1
                    break
        

    def contains(self, key: int) -> bool:
        pos = key%10000

        if self.st[pos] == key: return True
        else:
            for i in range(pos, 10000):
                if self.st[i] == key: return True
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)