class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        print(salary)
        _sum=0
        for i in range(1, len(salary)-1):
            _sum+=salary[i]
        
        return (_sum/(len(salary)-2))