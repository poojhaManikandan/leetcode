class Solution(object):
    def largestAltitude(self, gain):
        a=0
        b=0
        n=len(gain)
        res=[n]
        res[0]=0
        for i in gain:
            a=i
            c=b+a
            res.append(c)
            b=c
        return max(res)