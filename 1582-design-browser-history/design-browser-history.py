class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = Node(homepage)
        self.curr = self.root
        

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.prev = self.curr
        self.curr.next = newNode
        self.curr = newNode

        
    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url
        

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)