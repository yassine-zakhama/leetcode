class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        if n < 3:
            return tri[n]

        while n != 3:
            n -= 1
            new = sum(tri)
            tri[0] = tri[1]
            tri[1] = tri[2]
            tri[2] = new

        return sum(tri)
