class RandomizedSet:

    def __init__(self):
        self.Rset=set()
        

    def insert(self, val: int) -> bool:
        if val in self.Rset:
            return False
        else:
            self.Rset.add(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.Rset:
            self.Rset.discard(val)
            return True
        return False
        
    def getRandom(self) -> int:
        # random=self.Rset.pop()
        # self.Rset.add(random)
        return random.choice(list(self.Rset))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()