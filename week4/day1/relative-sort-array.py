class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic=defaultdict(int)
        ans=[]
        temp=[]
        for n in arr1:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        print(dic)
        for num in arr2:
            ans.extend([num]*dic[num])
            dic[num]=0
        print(dic)
        for k, v in dic.items():
            if dic[k] != 0:
                temp.extend([k]*v)
        temp=sorted(temp)
        ans.extend(temp)
        print(temp)
        return ans
        
                    
                    
                    
                
        