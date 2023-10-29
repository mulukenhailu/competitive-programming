class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if stack and c==")" and stack[-1]=="(":
                stack.pop()
            elif stack and c=="]" and stack[-1]=="[":
                stack.pop()
            elif stack and c=="}" and stack[-1]=="{":
                stack.pop()
            else:
                stack.append(c)
        return stack==[]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dic={}
#         valid=[]
#         for symboll in s:
#             if symboll== "}":
#                 dic[symboll]="{"
#             if symboll== "]":
#                 dic[symboll]="["
#             if symboll== ")":
#                 dic[symboll]="("
#         for i, par in enumerate(s):
#             if par not in dic:
#                 valid.append(par)
#             elif par in dic and len(valid)==0:
#                 return False
#             elif par in dic and i!=0:
#                 if dic[par] == valid[-1]:
#                     valid.pop()
#                 else:
#                     return False

#         return valid==[] 