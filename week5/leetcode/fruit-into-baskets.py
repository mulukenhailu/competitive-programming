class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l=0
        seen={}
        max_len=0

        for r in range(len(fruits)):

            if fruits[r] in seen:
                seen[fruits[r]]+=1
            else:
                seen[fruits[r]]=1

            if len(seen)>2:
                max_len=max(max_len, r-l)
                while len(seen)>2:
                    seen[fruits[l]]-=1
                    if seen[fruits[l]]==0:
                        del seen[fruits[l]]
                    l+=1
            
        return max(max_len, r-l+1)


        