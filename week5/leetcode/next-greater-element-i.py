class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        ans=[]

        for poper in nums2:
            while stack and stack[-1]<poper:
                poped=stack.pop()
                dic[poped]=poper
            stack.append(poper)
            
        print(dic)

        for num in nums1:
            if num in dic:
                ans.append(dic[num])
            else:
                ans.append(-1)
        
        return ans