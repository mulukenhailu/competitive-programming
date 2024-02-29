class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [float("-inf")] + arr + [float("-inf")] 
        ans = 0 
        stack = [] 
        for i, num in enumerate(arr): 
            while stack and arr[stack[-1]] > num: 
                curindex = stack.pop() 
                curnum = arr[curindex]
                leftBound = stack[-1]
                rightBound = i
                ans += curnum * (curindex - leftBound) * (rightBound - curindex)  
            stack.append(i) 
        return ans % (10 ** 9 + 7)


        
        