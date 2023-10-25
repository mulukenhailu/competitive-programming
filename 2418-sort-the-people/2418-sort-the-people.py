class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={}
        for h, n in zip(heights, names):
            dic[h]=n
        dic=dict(sorted(dic.items(), key=lambda item : item[0], reverse=True))
        ans=[]
        print(dic)
        for k, v in dic.items():
            ans.append(v)
        return ans
        
    
            
        