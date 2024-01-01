class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if len(arr)<3:
            return False
        for i in range(n-1):
            if arr[i]==arr[i+1]:
                return False
            elif arr[i]>arr[i+1]:
                break
        
        if i==0:
            return False
        for j in range(i, n-1):
            if arr[j]<arr[j+1] or arr[j]==arr[j+1]:
                return False
        return True
            

        