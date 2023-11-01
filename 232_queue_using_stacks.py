class MyQueue(object):
    from collections import deque

    def __init__(self):
        self.stack_one = deque()
        self.stack_two = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_one.append(x)


    def pop(self):
        """
        :rtype: int
        """
        ### 每一次都倒腾一遍
        # while len(self.stack_one):
        #     tmp = self.stack_one.pop()
        #     self.stack_two.append(tmp)
        # ans =  self.stack_two.pop()
        # while len(self.stack_two):
        #     tmp = self.stack_two.pop()
        #     self.stack_one.append(tmp)
        # return ans


        if len(self.stack_two):
            ans = self.stack_two.pop()
        else:
            while len(self.stack_one):
                self.stack_two.append(self.stack_one.pop())
            ans = self.stack_two.pop()
        return ans


    def peek(self):
        """
        :rtype: int
        """
        ### 每一次都倒腾一遍
        # while len(self.stack_one):
        #     tmp = self.stack_one.pop()
        #     self.stack_two.append(tmp)
        # ans = self.stack_two.pop()
        # self.stack_one.append(ans)
        # while len(self.stack_two):
        #     tmp = self.stack_two.pop()
        #     self.stack_one.append(tmp)
        # return ans
        if len(self.stack_two):
            ans = self.stack_two.pop()
            self.stack_two.append(ans)
        else:
            while len(self.stack_one):
                self.stack_two.append(self.stack_one.pop())
            ans = self.stack_two.pop()
            self.stack_two.append(ans)
        return ans


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack_one) or len(self.stack_two):
            return False
        else:
            return True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
