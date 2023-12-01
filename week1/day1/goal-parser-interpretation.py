class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        i=0
        for i in range(len(command)):
            if command[i]=="G":
                ans+="G"
            elif command[i]=="(" and command[i+1]==")":
                ans+="o"
            elif command[i]=="(" and command[i+1]=="a":
                ans+="al"
            else:
                 # elif command[i]==")" or "a" or "l" :
                pass
        return ans
        