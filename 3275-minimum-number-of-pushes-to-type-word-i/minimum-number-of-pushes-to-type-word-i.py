class Solution(object):
    def minimumPushes(self, word):
        q,r=divmod(len(word),8)
        return ((q<<2)+r)*(q+1)
        