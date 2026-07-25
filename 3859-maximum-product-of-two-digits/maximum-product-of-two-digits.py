class Solution(object):
    def maxProduct(self, n):
        lis=list(map(int, str(n)))
        h1=max(lis)
        lis.remove(h1)
        h2=max(lis)
        return h1*h2
