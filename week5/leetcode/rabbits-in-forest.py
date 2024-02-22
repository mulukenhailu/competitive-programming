class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=defaultdict(list)
        ans=0

        for a in answers:
            dic[a].append(a)

        print(dic)

        for v in dic.values():
            if v[0]==0:
                ans+=len(v)
                print(ans)
            elif v[0]==1 and len(v)%2:
                ans+=len(v)+1
                print(ans)
            elif v[0]==1 and len(v)%2==0:
                ans+=len(v)
                print(ans)
            else:
                n=len(v)
                if n==1:
                    ans+=v[0]+1
                else:
                    ans+=((v[0]+n)//(v[0]+1))*(v[0]+1)


        return ans
        