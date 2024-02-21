# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen=set()
        hA=headA
        while hA:
            seen.add(hA)
            hA=hA.next
        hB=headB
        while hB:
            # check memory location
            if hB in seen:
                return hB
            hB=hB.next
        return 


        