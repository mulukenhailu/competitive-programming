class Robot:

    def __init__(self, width: int, height: int):
        self.direction="East"
        self.location=[0,0]
        self.width=width
        self.height=height
        self.totalStep=0

    def step(self, num: int) -> None:
        width=self.width-1
        height=self.height-1
        temp1=num
        self.totalStep+=num
        num=num%(2*(width+height))
        while num>0:

            if self.direction=="East":   
                self.location[0]+=num
                temp=self.location[0]
                if self.location[0]>width:
                    self.location[0]=width
                    num=temp-width
                    self.direction="North"
                else:
                    num=0

            if self.direction=="North":
                self.location[1]+=num
                temp=self.location[1]
                if self.location[1]>height:
                    self.location[1]=height
                    num=temp-height
                    self.direction="West"   
                else:
                    num=0

            if self.direction=="West":
                self.location[0]-=num
                temp=self.location[0]
                if self.location[0]<0:
                    self.location[0]=0
                    num=abs(temp)
                    self.direction="South"
                else:
                    num=0

            if self.direction=="South":
                self.location[1]-=num
                temp=self.location[1]
                if self.location[1]<0:
                    self.location[1]=0
                    num=abs(temp)
                    self.direction="East"
                else:
                    num=0

        if temp1>0 and num==0 and self.location==[0,0] and self.totalStep!=0:
            self.direction="South"

    def getPos(self) -> List[int]:
        return self.location

    def getDir(self) -> str:
        return self.direction


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()