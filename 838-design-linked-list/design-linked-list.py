class MyLinkedList:

    def __init__(self):
        self.store = []
        

    def get(self, index: int) -> int:
        if index > len(self.store) -1:
            return -1
        return self.store[index]
        

    def addAtHead(self, val: int) -> None:
        self.store.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.store.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self.store):
            self.store.insert(index, val)
        elif index == len(self.store):
            self.store.append(val)
        

    def deleteAtIndex(self, index: int) -> None:
        if index > len(self.store) - 1:
            return
        self.store.pop(index)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)