class Node:
    def __init__(self, value):
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity=capacity
        self.map={}

        self.head=Node(-1)

        self.tail=Node(-1)

        self.tail.prev=self.head
        self.head.next=self.tail

    
    def get(self, key: int) -> int:
        # map-->key:Node
        # currentNode=map[key]
       
        if key in self.map:
            currentNode=self.map[key]

            # deleteNode-->function()
            prevNode=currentNode.prev
            nextNode=currentNode.next
            
            prevNode.next=nextNode
            nextNode.prev=prevNode

            # put the deleted node before the tail
            beforeTail=self.tail.prev

            beforeTail.next=currentNode
            currentNode.prev=beforeTail

            currentNode.next=self.tail
            self.tail.prev=currentNode

            return currentNode.value

        else:
            return -1
    
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value

            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            before_tail = self.tail.prev
            
            before_tail.next = node
            node.prev = before_tail
            node.next = self.tail
            self.tail.prev = node
        else:
           
            if len(self.map) >= self.capacity:
                lru_node = self.head.next
                del self.map[lru_node.key] 
                self.head.next = lru_node.next
                lru_node.next.prev = self.head

            new_node = Node(value)
            new_node.key = key
            before_tail = self.tail.prev
            before_tail.next = new_node
            new_node.prev = before_tail
            new_node.next = self.tail
            self.tail.prev = new_node

            self.map[key] = new_node



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)