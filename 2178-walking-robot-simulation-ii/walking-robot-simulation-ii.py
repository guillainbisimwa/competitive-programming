class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.str = ["East", "North", "West", "South"]
        self.d = 0
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.loop = (width + height - 2) * 2
        

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        num %= self.loop
        if num == 0:
            num = self.loop
        if self.d == 0:
            if self.x + num < self.w:
                self.x += num
            else:
                num -= self.w - self.x - 1
                self.x = self.w - 1
                self.d = 1
                self.step(num)
        elif self.d == 1:
            if self.y + num < self.h:
                self.y += num
            else:
                num -= self.h - self.y - 1
                self.y = self.h - 1
                self.d = 2
                self.step(num)
        elif self.d == 2:
            if self.x >= num:
                self.x -= num
            else:
                num -= self.x
                self.x = 0
                self.d = 3
                self.step(num)
        elif self.d == 3:
            if self.y >= num:
                self.y -= num
            else:
                num -= self.y
                self.y = 0
                self.d = 0
                self.step(num)
        

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.x, self.y]

        

    def getDir(self):
        """
        :rtype: str
        """
        return self.str[self.d]


        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()