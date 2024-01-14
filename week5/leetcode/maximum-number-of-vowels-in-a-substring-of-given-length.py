class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=('a', 'e', 'i', 'o', 'u')
        l=0
        ans=0
        max_vowel=float("-inf")
        
        for r in range(len(s)):
            if s[r] in vowel:
                ans+=1
            while r-l+1==k:
                max_vowel=max(max_vowel, ans)
                if s[l]  in vowel:
                    ans-=1
                l+=1

        print(max_vowel)
        return max_vowel

                

            


            
            



        