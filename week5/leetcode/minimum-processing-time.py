class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        lst=[]
        pos=[]

        for i in range(len(tasks)):
            if (i+1)%4==0:
                lst.append(tasks[i])
        
        for p, t in zip(processorTime, lst):
            pos.append(p+t)

        return max(pos)




        