class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yc = []
        nc = [0]
        yct, nct =0,0
        for i in range(len(customers)):
            if customers[i] == "N":
                nct +=1
            nc.append(nct)
            if customers[~i] == "Y":
                yct +=1
            yc.append(yct)
        yc.reverse()
        yc.append(0)
        temp = float('inf')
        for i in range(len(yc)-1, -1,-1):
            if yc[i] + nc[i] <= temp:
                temp = yc[i]  + nc[i]
                ans = i
        return ans
                
       