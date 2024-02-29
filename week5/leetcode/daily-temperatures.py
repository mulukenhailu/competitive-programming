class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        largeTemp=[]
        numofDay=[0]*len(temperatures)
        for i, temp in enumerate(temperatures):    
            while largeTemp and temp > temperatures[largeTemp[-1]]:
                currentindex=largeTemp.pop()
                numofDay[currentindex]=i-currentindex
            largeTemp.append(i)
        return numofDay
        
        