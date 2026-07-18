import fractions as f
class Solution(object):
    def findGCD(self, nums):
        m=min(nums)
        ma=max(nums)
        return f.gcd(m,ma)