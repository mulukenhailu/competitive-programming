class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=len(heights)
        dic=defaultdict()
        for h, n in zip(heights, names):
            dic[h]=n
        
        for i in range(l):
            for j in range(i+1, l):
                if heights[i]>heights[j]:
                    heights[i], heights[j]=heights[j], heights[i]
    
        return [dic[h] for h in heights[::-1]]
            
        
        
    
            
        