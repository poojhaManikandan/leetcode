
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        even=0
        odd=0
        for i in range(n*2):
            if i%2 == 0:
                even+=i
            else:
                odd+=i
        while even:
            odd,even = even,odd%even
        return odd        