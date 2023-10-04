'''
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def do(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x 
            res = do(x,n/2)
            if n % 2 == 0:
                return res*res
            else:
                return res*res*x

        if n < 0:
            x = 1/x 
            n = -n
        return do(x, n)
