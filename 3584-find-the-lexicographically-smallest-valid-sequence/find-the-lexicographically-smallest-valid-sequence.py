class Solution(object):
    def validSequence(self, word1, word2):
        m,n=len(word1),len(word2)
        mtc=[-1]*n
        i,j=m-1,n-1
        while i>=0 and j>=0:
            if word1[i]==word2[j]:
                mtc[j]=i
                j-=1
            i-=1
        i=j=0
        res=[]
        ch=False
        while i<m and j<n:
            if word1[i]==word2[j]:
                res.append(i)
                j+=1
            elif not ch and (j==n-1 or mtc[j+1]>i):
                ch=True
                res.append(i)
                print(i)
                j+=1
            i+=1
        return res if j==n else []       