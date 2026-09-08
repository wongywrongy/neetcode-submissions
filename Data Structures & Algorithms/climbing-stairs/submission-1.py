class Solution:
    def climbStairs(self, n: int) -> int:
        # starting value a = way to climb stairs (i - 1), b = ways to climb i stairs
        a, b = 1, 1

        # each pass moves the window forward (sliding window of 2 because a and b) 
        for _ in range(n-1):
            # new a = old b
            a, b = b, a + b

        return b