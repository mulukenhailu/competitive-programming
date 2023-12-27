class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={h:n for h, n in zip(heights, names)}
        arr=[0]*(max(heights)+1)
        ans=[]
        for h in heights:
            pre=arr[h]
            arr[h]=pre+1
        for i, v in enumerate(arr):
            if v !=0:
                for _ in range(v):
                    ans.append(i)
        print(ans)
        return [dic[h] for h in ans[::-1]]
                
            