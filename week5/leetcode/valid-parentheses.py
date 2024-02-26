class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for p in s:
            if stack:
                if p==")":
                    poped=stack.pop()
                    if poped != "(":
                        return False
                elif p=="]":
                    poped=stack.pop()
                    if poped != "[":
                        return False
                elif p=="}":
                    poped=stack.pop()
                    if poped != "{":
                        return False
                else:
                    stack.append(p)
            else:
                stack.append(p)

        return stack==[]