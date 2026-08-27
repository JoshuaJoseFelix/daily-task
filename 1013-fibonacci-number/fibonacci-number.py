class Solution(object):
    def fib(self, n):
       
        one, two = 0, 1

        for _ in range(n):
            one, two = two, one + two

        return one