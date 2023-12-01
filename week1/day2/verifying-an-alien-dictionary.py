class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        c = {order[i]: i for i in range(len(order))}
        for i in range(1,len(words)):
            a, b = words[i-1], words[i]
            for j in range(len(a)):
                if j == len(b):
                    return False
                ca, cb = a[j], b[j]
                aord, bord = c[ca], c[cb]
                if aord < bord:
                    break
                if aord > bord: 
                    return False
        return True   