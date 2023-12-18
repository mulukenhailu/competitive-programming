class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dictt=defaultdict(list)
        for p in paths:
            path=p.split(" ")
            f=path[0]
            for s in path[1:]:
                s=s.split(".txt")
                n=s[0]
                c=s[1]
                dictt[c].append((f, n))
                    
        print(dictt)
        ans=[]
        for k, v in dictt.items():
            if len(v)>1:
                temp=[]
                for p, n in v:
                    temp.append(p+"/"+n+".txt")
                ans.append(temp)
                
        return ans
            