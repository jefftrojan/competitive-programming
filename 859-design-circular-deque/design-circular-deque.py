class MyCircularDeque:

    def __init__(self, k: int):
        self.q = []
        self.k = k
        
    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.k:
            self.q = [value] + self.q
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        return False
        
    def deleteFront(self) -> bool:
        if len(self.q) > 0:
            self.q.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.q) > 0:
            self.q.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.q) > 0:
            front = self.q[0]
            return front
        return -1

    def getRear(self) -> int:
        if len(self.q) > 0:
            last = self.q[-1]
            return last
        return -1
        
    def isEmpty(self) -> bool:
        if len(self.q) == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if len(self.q) == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()