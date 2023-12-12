class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        template=strs[0]
        matching=len(template)
        for i in range(1, len(strs)):
            count=0
            loop=min(len(strs[i]), matching)
            for j in range(loop):
                if strs[i][j]==template[j]:
                    # print(strs[i][j], template[j])
                    count+=1
                else:
                    break
            
            matching=min(count, matching)
        return template[:matching]
    
    
    
    # in collaboration with my head of education Million  12/12/2023
            