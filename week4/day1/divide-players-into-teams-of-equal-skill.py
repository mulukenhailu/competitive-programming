class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l=0
        r=len(skill)-1
        ans=[]
        if len(skill)==2:
            return skill[0]*skill[1]
        elif sum(skill)%(len(skill)/2) != 0:
            return -1
        else:
            skill=sorted(skill)
            temp=skill[l]+skill[r]
            while l<r:
                ctemp=skill[l]+skill[r]
                if ctemp != temp:
                    return -1
                else:
                    ans.append(skill[l]*skill[r])
                l+=1
                r-=1
        return sum(ans)
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         tot=0
        
#         for num in skill:
#             tot+=num
            
#         target=(tot)/(len(skill)/2)
        
#         if target%1!=0:
#             return -1
        
#         for num in skill:
#             if num>=target:
#                 return -1
        
#         skill=sorted(skill)
#         i=0
#         j=len(skill)-1
#         ans=0
#         while i<=j:
#             if (skill[i]+skill[j])==target:
#                 ans+=(skill[i]*skill[j])
#                 i+=1
#                 j-=1
#             else:
#                 return -1
#         return ans

        
        
        
        