class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            if n>=10:
                q,r=divmod(n,10)
            else:
                q=1
                r=n
            pro=q*r
            print(pro)
            if pro%t==0:
                return n
            n=n+1
            print(n)
            

                


        