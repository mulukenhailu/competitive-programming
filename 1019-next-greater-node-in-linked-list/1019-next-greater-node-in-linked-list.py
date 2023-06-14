# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
#         if not head.next:
#             return [0]
#         stk=[]
#         slow=head
#         while slow and slow.next:
#             fast=slow.next
#             while fast:
#                 if slow.val < fast.val:
#                     stk.append(fast.val)
#                     break
#                 fast=fast.next
#             else:
#                  stk.append(0)
                
#             slow=slow.next
#         else:
#             stk.append(0)
#         return stk
             
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        final=[0]*len(arr)
        stk=[]
        for i, v in enumerate(arr):
            while stk and arr[stk[-1]]<v:
                minn=stk.pop()
                final[minn]=v
            stk.append(i)
        return final
        