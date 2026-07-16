class Solution(object):
    def uniqueOccurrences(self, arr):
        dict={}
        val=1
        for i in arr:
            dict[i]=dict.get(i,0)+1
        arr=list(dict.values())
        uni=len(arr)==len(set(arr))
        return uni

            
