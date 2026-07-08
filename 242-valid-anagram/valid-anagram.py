class Solution(object):
    def isAnagram(self, s, t):
        a=sorted(s)
        b=sorted(t)
        if a==b:
            return True
        else:
            return  False
        