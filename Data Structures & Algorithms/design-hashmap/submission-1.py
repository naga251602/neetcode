class MyHashMap:

    def __init__(self):
        self.hm = [[-1, -1] for i in range(0, 10000)] 

    def put(self, key: int, value: int) -> None:
        pos = key%10000
        if self.hm[pos][0] == -1 or self.hm[pos][0] == key: 
            self.hm[pos][0], self.hm[pos][1] = [key, value]
        else:
            for i in range(pos, 10000):
                if self.hm[i][0] == -1: 
                    self.hm[i][0], self.hm[i][1] = [key, value]
                    break

        

    def get(self, key: int) -> int:
        pos = key%10000

        if self.hm[pos][0] == key: return self.hm[pos][1]
        else:
            for i in range(pos, 10000):
                if self.hm[i][0] == key: return self.hm[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        pos = key%10000

        if self.hm[pos][0] == key: 
            self.hm[pos][0], self.hm[pos][1] = [-1, -1]
        else:
            for i in range(pos, 10000):
                if self.hm[i][0] == key: 
                    self.hm[i][0], self.hm[i][1] = [-1, -1]
                    break

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)