class Solution(object):
    def smallestSubsequence(self, s):
        last = {ch: i for i, ch in enumerate(s)}

        vis = set()     
        ans = []        
        for i, ch in enumerate(s):
         
            if ch in vis:
                continue
            while (ans and
                   ans[-1] >= ch and
                   last[ans[-1]] >= i):

                vis.remove(ans.pop())
            ans.append(ch)
            vis.add(ch)

        return "".join(ans)

        