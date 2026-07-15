class Solution(object):
    def countBits(self, n):
        res=[]
        for i in range(n+1):
            bit=bin(i)
            arr=list(bit)
            cou=arr.count('1')
            res.append(cou)
        return res


        
        