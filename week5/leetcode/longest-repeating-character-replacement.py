class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0 
        start = 0 
        freq = {}
        max_freq = 0 
        for end in range(len(s)):
            char = s[end]
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])
            while end - start + 1 - max_freq > k:
                freq[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len

        
          