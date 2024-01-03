class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        ans=0
        while l<=r:
            if people[l]+people[r]>limit:
                r-=1
                ans+=1
            elif people[l]+people[r]==limit:
                r-=1
                l+=1
                ans+=1
            else:
                r-=1
                l+=1
                ans+=1
        return ans
