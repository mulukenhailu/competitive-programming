class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList=path.split("/")
        stack=[]
        print(pathList)

        for p in pathList:
            if stack and p=="..":
                stack.pop()
            elif p != "" and p!=".." and p!=".":
                stack.append(p)
        print(stack)

        return "/" + "/".join(stack)

        

        