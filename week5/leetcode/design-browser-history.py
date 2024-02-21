class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
        self.prev=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_page=Node(homepage)
        
    def visit(self, url: str) -> None:
        new_page=Node(url)

        new_page.prev=self.cur_page
        self.cur_page.next=new_page
        
        self.cur_page=new_page


    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur_page.prev:
                self.cur_page=self.cur_page.prev
            else:
                break
        return self.cur_page.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur_page.next:
                self.cur_page=self.cur_page.next
            else:
                break
        return self.cur_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)