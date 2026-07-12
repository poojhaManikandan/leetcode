class Solution(object):
    def reverseWords(self, s):
        str=[]
        str=s.split()
        str=str[::-1]
        return " ".join(str)