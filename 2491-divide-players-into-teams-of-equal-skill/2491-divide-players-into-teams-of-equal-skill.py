class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot=0
        
        for num in skill:
            tot+=num
            
        target=(tot)/(len(skill)/2)
        
        if target%1!=0:
            return -1
        
        for num in skill:
            if num>=target:
                return -1
        
        skill=sorted(skill)
        i=0
        j=len(skill)-1
        ans=0
        while i<=j:
            if (skill[i]+skill[j])==target:
                ans+=(skill[i]*skill[j])
                i+=1
                j-=1
            else:
                return -1
        return ans

        
        
        
        