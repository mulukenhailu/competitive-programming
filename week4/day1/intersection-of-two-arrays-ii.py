class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_c=Counter(nums1)
        num2_c=Counter(nums2)
        print(num1_c)
        print(num2_c)
        ans=[]
        for k in num1_c:
            if k in num2_c:
                temp=(min(num1_c[k], num2_c[k]))
                for _ in range(temp):
                    ans.append(k)
        return ans
        

        