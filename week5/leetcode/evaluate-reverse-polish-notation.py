class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst=[]
        if len(tokens)==1:
            return int(tokens[-1])
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                lst.append(int(token))
            else:
                if token=="+":
                    lst.append(lst.pop()+lst.pop())
                if token=="-":
                    fnum, snum=lst.pop(), lst.pop()
                    lst.append(snum-fnum)
                if token=="*":
                    lst.append(lst.pop()*lst.pop())
                if token=="/":
                    fnum, snum=lst.pop(), lst.pop()
                    lst.append(int(snum/fnum))
        return lst[-1]
        