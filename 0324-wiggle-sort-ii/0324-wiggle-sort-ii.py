class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n=len(nums)
        
        if n%2==0:
            ans=[]
            mid=n//2
            maxheap1=[]
            maxheap2=[]
            for num in (nums[:mid]):
                maxheap1.append(-num)
            for num in (nums[mid:]):
                maxheap2.append(-num)
            heapq.heapify(maxheap1)
            heapq.heapify(maxheap2)
            print(maxheap1)
            print(maxheap2)
            for _ in range(mid):
                ans.append(-heapq.heappop(maxheap1))
                ans.append(-heapq.heappop(maxheap2))
            nums[::]=ans[::]
        else:
            ans=[]
            mid=n//2
            ans.append(nums[mid])
            maxheap1=[]
            maxheap2=[]
            for num in (nums[:mid]):
                maxheap1.append(-num)
            for num in (nums[mid+1:]):
                maxheap2.append(-num)
            heapq.heapify(maxheap1)
            heapq.heapify(maxheap2)
            print(maxheap1)
            print(maxheap2)
            for _ in range(mid):
                ans.append(-heapq.heappop(maxheap2))
                ans.append(-heapq.heappop(maxheap1))
            nums[::]=ans[::]
            
            