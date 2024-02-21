# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        ans = []

        if n < k:
            ptr = head
            while ptr:
                ans.append(ListNode(ptr.val))  
                ptr = ptr.next
            for i in range(k - n):
                ans.append(None)  

        else:
            size, remainder = divmod(n, k)
            ptr = head
            for i in range(k):
                part_head = ptr
                for j in range(size + (i < remainder) - 1):
                    ptr = ptr.next
                if ptr:
                    next_ptr = ptr.next
                    ptr.next = None  
                    ptr = next_ptr  
                ans.append(part_head)  

        return ans
        