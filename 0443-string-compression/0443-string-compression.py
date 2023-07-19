class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        right = -1
        left = 0
        write = 0  
        
        while right < len(chars):
            while right + 1 < len(chars) and chars[left] == chars[right + 1]:
                right += 1
                
            chars[write] = chars[left]  
            write += 1
            count = right - left + 1
            
            if count > 1:
                for digit in str(count): 
                    chars[write] = digit
                    write += 1
            
            left = right + 1
            right = left
        
        return write  
