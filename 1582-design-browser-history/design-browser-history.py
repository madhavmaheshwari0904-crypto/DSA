class Node:
    def __init__(self,url):
        self.prev=None
        self.url=url
        self.next=None
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr=Node(homepage)
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr.next=Node(url)
        self.curr.next.prev=self.curr
        self.curr=self.curr.next
    def back(self, step):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr.prev and step>0:
            self.curr=self.curr.prev
            step-=1
        return self.curr.url
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr.next and steps>0:
            self.curr=self.curr.next
            steps-=1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)