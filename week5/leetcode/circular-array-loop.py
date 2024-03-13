class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        for idx in range(n):
            seen=set()
            while True:
                if idx in seen:             
                    return True
                seen.add(idx)
                curpos=idx
                idx=(idx + nums[idx] ) % n  
                # idx next postion after jump     
                if curpos == idx or (nums[idx] > 0) != (nums[curpos]>0):        
                    break       

        return False