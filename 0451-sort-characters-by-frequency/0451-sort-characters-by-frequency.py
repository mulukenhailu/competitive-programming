class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for char in s:
            if char in dic:
                dic[char]+=1
            else:
                dic[char]=1
        dic= sorted(dic.items(), key=lambda item: item[1], reverse=True)
        res=""
        for char, count in dic:
            res+=char*count
        return res