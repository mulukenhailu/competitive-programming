class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        intersection=[]
        common=[]
        
        for idx, string in  enumerate(list1):
            if string in list2:
                intersection.append([idx, list2.index(string), idx+list2.index(string)])
                
        intersection.sort(key=lambda x:x[2])
        firstintersection=intersection[0][2]
        
        for intersect in intersection:
            if intersect[2]==firstintersection:
                common.append(list1[intersect[0]])
                
        return common
                
        