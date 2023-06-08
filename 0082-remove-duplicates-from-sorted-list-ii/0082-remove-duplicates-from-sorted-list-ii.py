# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        stack=[]
        temp=head
        
        while temp:
            stack.append(temp.val)
            temp=temp.next
            
        dic=Counter(stack)
        stk=[]
        
        for k, v in dic.items():
            if v==1:
                stk.append(k)
        
        dum=ListNode(0)
        temp2=dum
        
        for num in stk:
            dum.next=ListNode(num)
            dum=dum.next
            
        return temp2.next
        
                
            